import datetime
import frontmatter
import jinja2
import os
import pathlib
import shutil
import subprocess
import tempfile
import tomllib


def initialize_site(site_path, site_posts_path, site_style_path, style_path):
	shutil.rmtree(site_path, ignore_errors=True)
	site_posts_path.mkdir(parents=True)
	shutil.copyfile(style_path, site_style_path)
	shutil.copyfile("cv.pdf", site_path / "cv.pdf")


def read_post(path, posts_href):
	post = frontmatter.load(path)
	post.content = f"# {post['title']}\n\n{post.content}"
	post["source"] = frontmatter.dumps(post)
	post["href"] = f"{posts_href}/{path.stem}.html"
	post["path"] = path
	post["timestamp"] = post["time"]

	if path.stem.startswith("_"):
		return post

	post["time"] = datetime.datetime.strptime(post["time"], "%Y-%m-%d %H:%M").strftime("%Y-%m-%d")
	return post


def get_posts(post_paths, posts_href):
	posts = [read_post(path, posts_href) for path in post_paths]
	posts = sorted(posts, key=lambda post: post["timestamp"], reverse=True)
	return posts


def create_site_post(post, site_path, template_path):
	args = ["pandoc"]
	args.append("--from=markdown-implicit_figures")
	args.append("--highlight-style=pygments")
	args.append("--katex=https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/")
	args.extend(["--output", str(site_path / post["path"].with_suffix(".html").name)])
	args.append(f"--template={template_path}")
	subprocess.run(args, check=True, input=post["source"], text=True)


def create_site_index(cfg, posts, site_path, site_style_path, template):
	page = template.render(
		icon=cfg["paths"]["icon"],
		posts=[post for post in posts if not post["path"].stem.startswith("_")],
		style=pathlib.Path(os.path.relpath(site_style_path, site_path)).as_posix(),
		title=cfg["title"]
	)
	(site_path / "index.html").write_text(page)


def create_site_posts(cfg, posts, site_posts_path, site_style_path, template):
	pandoc_template = template.render(
		article="$body$",
		icon=cfg["paths"]["icon"],
		pandoc=True,
		style=pathlib.Path(os.path.relpath(site_style_path, site_posts_path)).as_posix(),
		title="$pagetitle$"
	)
	with tempfile.TemporaryDirectory() as temporary_path:
		template_path = pathlib.Path(temporary_path) / "template.html"
		template_path.write_text(pandoc_template)
		for post in posts:
			create_site_post(post, site_posts_path, template_path)


if __name__ == "__main__":
	with pathlib.Path("config.toml").open("rb") as f:
		cfg = tomllib.load(f)

	posts_path = pathlib.Path("posts")
	site_path = pathlib.Path("_site")
	site_posts_path = site_path / posts_path
	style_path = pathlib.Path("template.css")
	site_style_path = site_path / style_path
	initialize_site(site_path, site_posts_path, site_style_path, style_path)
	posts = get_posts(posts_path.glob("*.md"), posts_path.as_posix())
	template = jinja2.Environment(
		autoescape=True,
		loader=jinja2.FileSystemLoader("."),
		lstrip_blocks=True,
		trim_blocks=True
	).get_template("template.xml")
	create_site_index(cfg, posts, site_path, site_style_path, template)
	create_site_posts(cfg, posts, site_posts_path, site_style_path, template)
