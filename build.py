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
	args.append("--katex=https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/")
	args.extend(["--output", str(site_path / post["path"].with_suffix(".html").name)])
	args.append(f"--template={template_path}")
	subprocess.run(args, check=True, input=post["source"], text=True)


def create_site_index(cfg, posts, site_path, site_style_path, template):
	page = template.render(
		favicon=cfg["paths"]["favicon"],
		name=cfg["name"],
		posts=[post for post in posts if not post["path"].stem.startswith("_")],
		style=pathlib.Path(os.path.relpath(site_style_path, site_path)).as_posix(),
		title=cfg["title"],
		url=cfg["paths"]["url"]
	)
	(site_path / "index.html").write_text(page)


def create_site_posts(cfg, posts, site_posts_path, site_style_path, template):
	pandoc_template = template.render(
		article="$body$",
		favicon=cfg["paths"]["favicon"],
		name=cfg["name"],
		pandoc=True,
		style=pathlib.Path(os.path.relpath(site_style_path, site_posts_path)).as_posix(),
		title="$pagetitle$",
		url=cfg["paths"]["url"]
	)
	with tempfile.TemporaryDirectory() as temporary_path:
		template_path = pathlib.Path(temporary_path) / "template.html"
		template_path.write_text(pandoc_template)
		for post in posts:
			create_site_post(post, site_posts_path, template_path)


if __name__ == "__main__":
	with pathlib.Path("config.toml").open("rb") as f:
		cfg = tomllib.load(f)

	paths = cfg["paths"]
	posts_path = pathlib.Path(paths["posts"])
	site_path = pathlib.Path(paths["site"])
	site_posts_path = site_path / posts_path
	style_path = pathlib.Path(paths["style"])
	site_style_path = site_path / style_path
	template_path = pathlib.Path(paths["template"])
	posts_href = site_posts_path.relative_to(site_path)
	post_paths = posts_path.glob("*.md")
	initialize_site(site_path, site_posts_path, site_style_path, style_path)
	posts = get_posts(post_paths, posts_href)
	template = jinja2.Environment(
		autoescape=True,
		loader=jinja2.FileSystemLoader(template_path.parent),
		lstrip_blocks=True,
		trim_blocks=True
	).get_template(template_path.name)
	create_site_index(cfg, posts, site_path, site_style_path, template)
	create_site_posts(cfg, posts, site_posts_path, site_style_path, template)
