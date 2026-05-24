import datetime
import html
import pathlib
import re
import unicodedata


def read_post(path):
	lines = path.read_text().splitlines()
	post = {
		line.split(": ", 1)[0]: line.split(": ", 1)[1]
		for line in lines[1:lines.index("---", 1)]
	}
	post["path"] = path
	return post


def slugify(title):
	slug = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
	slug = re.sub("'", "", slug)
	slug = re.sub("[^a-z0-9]+", "-", slug).strip("-")
	if slug:
		return slug
	return "post"


def format_date(date):
	date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
	return date.strftime("%B %Y")


def rename_posts(posts):
	old_paths = {post["path"] for post in posts}
	targets = [post["path"].with_name(f"{slugify(post['title'])}.md") for post in posts]
	if len(targets) != len(set(targets)):
		raise SystemExit("Multiple post titles resolve to the same filename.")
	for post, target in zip(posts, targets):
		if post["path"] == target:
			continue
		if target.exists() and target not in old_paths:
			raise SystemExit(f"{post['path']} wants to become {target}, but {target} already exists.")
		if post["path"].with_suffix(".md.tmp").exists():
			raise SystemExit(f"{post['path'].with_suffix('.md.tmp')} already exists.")
	for post, target in zip(posts, targets):
		if post["path"] != target:
			post["path"].rename(post["path"].with_suffix(".md.tmp"))
	for post, target in zip(posts, targets):
		tmp = post["path"].with_suffix(".md.tmp")
		if tmp.exists():
			tmp.rename(target)
			post["path"] = target


posts = [read_post(path) for path in pathlib.Path("posts").glob("*.md")]
rename_posts(posts)

posts = sorted(
	posts,
	key=lambda post: post["date"],
	reverse=True,
)

rows = "\n".join(
	(
		f"\t\t<tr>\n\t\t\t<td>{format_date(post['date'])}</td>\n"
		f"\t\t\t<td><a href=\"#\">{html.escape(post['title'], quote=False)}</a></td>\n\t\t</tr>"
	)
	for post in posts
)

path = pathlib.Path("index.html")
path.write_text(
	re.sub("<table main>.*?</table>", f"<table main>\n{rows}\n\t</table>", path.read_text(), count=1, flags=re.S)
)
