import html
import json
import pathlib
import re
import unicodedata


def create_page(index_source, post):
	nav_match = re.search(
		r"^(?P<indent>[\t ]*)<nav\b[^>]*>.*?</nav>",
		index_source,
		re.MULTILINE | re.DOTALL
	)
	closing_match = re.search(r"</body>\s*</html>\s*$", index_source)
	indent = nav_match.group("indent")
	post_body = html.escape(post["body"], quote=False).replace("\n", f"\n{indent}\t")
	article = (
		f"{indent}<article hidden>\n"
		f"{indent}\t{post_body}\n"
		f"{indent}</article>"
	)
	page_source = (
		index_source[:nav_match.end()]
		+ f"\n\n{article}\n"
		+ index_source[closing_match.start():]
	)
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
	blog_path = root_path / "blog"
	index_source = index_path.read_text(encoding="utf-8")
	posts = []
	for post_path in blog_path.glob("*.md"):
		post = read_post(post_path)
		slug_path = post_path.with_name(f"{create_slug(post['name'])}.md")
		if slug_path.exists() and not slug_path.samefile(post_path):
			raise FileExistsError()
		post_path.rename(slug_path)
		post["href"] = post.get("link", f"blog/{slug_path.stem}")
		post["target"] = " target=\"_blank\"" if "link" in post else ""
		posts.append(post)
	posts.sort(key=lambda post: post["name"])
	posts.sort(key=lambda post: post["date"], reverse=True)
	list_start = index_source.index("<dl>")
	list_indent = index_source[index_source.rfind("\n", 0, list_start) + 1:list_start]
	item_indent = f"{list_indent}\t"
	list_start += len("<dl>")
	list_end = index_source.index("</dl>", list_start)
	post_list = []
	previous_year = None
	for post in posts:
		year = post["date"][:4]
		displayed_year = year if year != previous_year else ""
		post_list.append(
			f"{item_indent}<dt>{displayed_year}</dt>\n"
			f"{item_indent}<dd><a href=\"{post['href']}\"{post['target']}>"
			f"{html.escape(post['name'], quote=False)}</a></dd>"
		)
		previous_year = year
	post_list = "\n".join(post_list)
	list_source = f"\n{post_list}\n{list_indent}"
	built_source = index_source[:list_start] + list_source + index_source[list_end:]
	playlist = json.loads((root_path / "opera.json").read_text(encoding="utf-8"))
	table_start = built_source.index("<table playlist>")
	table_indent = built_source[built_source.rfind("\n", 0, table_start) + 1:table_start]
	row_indent = f"{table_indent}\t"
	table_start += len("<table playlist>")
	table_end = built_source.index("</table>", table_start)
	table_rows = [
		f"{row_indent}<tr>\n"
		f"{row_indent}\t<th>What</th>\n"
		f"{row_indent}\t<th>Who</th>\n"
		f"{row_indent}\t<th>Where</th>\n"
		f"{row_indent}</tr>"
	]
	for opera in playlist:
		table_rows.append(
			f"{row_indent}<tr url=\"{html.escape(opera['url'], quote=True)}\">\n"
			f"{row_indent}\t<td>{html.escape(opera['what'])}</td>\n"
			f"{row_indent}\t<td>{html.escape(opera['who'])}</td>\n"
			f"{row_indent}\t<td>{html.escape(opera['where'])}</td>\n"
			f"{row_indent}</tr>"
		)
	table_source = "\n" + "\n".join(table_rows) + f"\n{table_indent}"
	built_source = built_source[:table_start] + table_source + built_source[table_end:]
	index_path.write_text(built_source, encoding="utf-8")
	for post in posts:
		if "link" in post:
			continue
		page_path = blog_path / f"{pathlib.Path(post['href']).name}.html"
		page_path.write_text(create_page(built_source, post), encoding="utf-8")
