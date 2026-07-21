import html
import pathlib
import re
import unicodedata


def create_slug(name):
	ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
	clean_name = re.sub(r"[^\w\s-]", "", ascii_name.lower())
	return re.sub(r"[-\s]+", "-", clean_name).strip("-_")


def read_post(post_path):
	front_matter = post_path.read_text(encoding="utf-8").split("---", 2)[1]
	return dict(line.split(": ", 1) for line in front_matter.strip().splitlines())


if __name__ == "__main__":
	index_path = pathlib.Path("index.html")
	index_source = index_path.read_text(encoding="utf-8")
	posts = []
	for post_path in pathlib.Path("posts").glob("*.md"):
		post = read_post(post_path)
		slug_path = post_path.with_name(f"{create_slug(post['name'])}.md")
		if slug_path.exists() and not slug_path.samefile(post_path):
			raise FileExistsError()
		post_path.rename(slug_path)
		posts.append(post)
	posts.sort(key=lambda post: post["name"])
	posts.sort(key=lambda post: post["date"], reverse=True)
	list_start = index_source.index("<dl>") + len("<dl>")
	list_end = index_source.index("</dl>", list_start)
	list_lines = index_source[list_start:list_end].splitlines()
	item_line = next(line for line in list_lines if line.strip())
	item_indent = item_line[:len(item_line) - len(item_line.lstrip())]
	list_indent = index_source[index_source.rfind("\n", 0, list_end) + 1:list_end]
	post_list = "\n\n".join(
		f"{item_indent}<dt>{post['date']}</dt>\n"
		f"{item_indent}<dd><a>{html.escape(post['name'])}</a></dd>"
		for post in posts
	)
	list_source = f"\n{post_list}\n{list_indent}"
	built_source = index_source[:list_start] + list_source + index_source[list_end:]
	index_path.write_text(built_source, encoding="utf-8")
