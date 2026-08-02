import html
import pathlib
import re
import unicodedata


def create_page(index_source, post):
	list_match = re.search(
		r"^(?P<indent>[\t ]*)<dl\b[^>]*>.*?</dl>",
		index_source,
		re.MULTILINE | re.DOTALL
	)
	indent = list_match.group("indent")
	post_body = html.escape(post["body"], quote=False).replace("\n", f"\n{indent}\t")
	article = (
		f"{indent}<article hidden>\n"
		f"{indent}\t{post_body}\n"
		f"{indent}</article>"
	)
	page_source = index_source[:list_match.start()] + article + index_source[list_match.end():]
	return re.sub(
		r"<title>.*?</title>",
		f"<title>{html.escape(post['name'], quote=False)}</title>",
		page_source,
		count=1,
		flags=re.DOTALL
	)


def create_slug(name):
	ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
	clean_name = re.sub(r"[^\w\s-]", "", ascii_name.lower())
	return re.sub(r"[-\s]+", "-", clean_name).strip("-_")


def read_post(post_path):
	_, front_matter, post_body = post_path.read_text(encoding="utf-8").split("---", 2)
	post = dict(line.split(": ", 1) for line in front_matter.strip().splitlines())
	post["body"] = post_body.strip()
	return post


if __name__ == "__main__":
	root_path = pathlib.Path(__file__).parent
	index_path = root_path / "index.html"
	posts_path = root_path / "posts"
	index_source = index_path.read_text(encoding="utf-8")
	posts = []
	for post_path in posts_path.glob("*.md"):
		post = read_post(post_path)
		slug_path = post_path.with_name(f"{create_slug(post['name'])}.md")
		if slug_path.exists() and not slug_path.samefile(post_path):
			raise FileExistsError()
		post_path.rename(slug_path)
		post["href"] = post.get("link", f"posts/{slug_path.stem}")
		post["target"] = " target=\"_blank\"" if "link" in post else ""
		posts.append(post)
	posts.sort(key=lambda post: post["name"])
	posts.sort(key=lambda post: post["date"], reverse=True)
	list_start = index_source.index("<dl>")
	list_indent = index_source[index_source.rfind("\n", 0, list_start) + 1:list_start]
	item_indent = f"{list_indent}\t"
	list_start += len("<dl>")
	list_end = index_source.index("</dl>", list_start)
	post_list = "\n".join(
		f"{item_indent}<dt>{post['date'][2:7]}</dt>\n"
		f"{item_indent}<dd><a href=\"{post['href']}\"{post['target']}>"
		f"{html.escape(post['name'], quote=False)}</a></dd>"
		for post in posts
	)
	list_source = f"\n{post_list}\n{list_indent}"
	built_source = index_source[:list_start] + list_source + index_source[list_end:]
	index_path.write_text(built_source, encoding="utf-8")
	for post in posts:
		if "link" in post:
			continue
		page_path = posts_path / f"{pathlib.Path(post['href']).name}.html"
		page_path.write_text(create_page(built_source, post), encoding="utf-8")
