import datetime
import jinja2
import pathlib
import shutil
import subprocess
import tempfile
import tomllib


def initialize_site(site_path, site_posts_path):
	shutil.rmtree(site_path, ignore_errors=True)
	site_posts_path.mkdir(parents=True)
	shutil.copyfile("index.css", site_path / "index.css")


def read_post(path):
	lines = path.read_text().splitlines()
	metadata_end = lines.index("---", 1) + 1
	post = {
		line.split(": ", 1)[0]: line.split(": ", 1)[1]
		for line in lines[1:metadata_end - 1]
	}
	post["href"] = f"posts/{path.stem}.html"
	post["path"] = path
	post["source"] = "\n".join(
		lines[:metadata_end]
		+ ["", f"# {post['title']}"]
		+ lines[metadata_end:]
	)
	post["timestamp"] = post["time"]
	post["time"] = datetime.datetime.strptime(
		post["time"],
		"%Y-%m-%d %H:%M"
	).strftime("%Y-%m-%d")
	return post


def get_posts(post_paths):
	posts = [read_post(path) for path in post_paths]
	posts = sorted(posts, key=lambda post: post["timestamp"], reverse=True)
	return posts


def render_post(post, site_path, template_path):
	args = ["pandoc"]
	args.append("--from=markdown-implicit_figures")
	args.append("--katex=https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/")
	args.extend([
		"--output",
		str(site_path / post["path"].with_suffix(".html").name)
	])
	args.append(f"--template={template_path}")
	subprocess.run(args, check=True, input=post["source"], text=True)


if __name__ == "__main__":
	site_path = pathlib.Path("_site")
	site_posts_path = site_path / "posts"
	posts_path = pathlib.Path("posts")
	post_paths = posts_path.glob("*.md")
	initialize_site(site_path, site_posts_path)
	posts = get_posts(post_paths)
	template = jinja2.Environment(
		autoescape=True,
		loader=jinja2.FileSystemLoader("."),
		lstrip_blocks=True,
		trim_blocks=True
	).get_template("template.html")
	with pathlib.Path("config.toml").open("rb") as f:
		config = tomllib.load(f)
	page = template.render(
		name=config["name"],
		posts=posts,
		title=config["title"]
	)
	(site_path / "index.html").write_text(page)
	pandoc_template = template.render(
		article="$body$",
		name=config["name"],
		pandoc=True,
		root="../",
		title="$pagetitle$"
	)
	with tempfile.TemporaryDirectory() as temporary_path:
		template_path = pathlib.Path(temporary_path) / "template.html"
		template_path.write_text(pandoc_template)
		for post in posts:
			render_post(post, site_posts_path, template_path)
