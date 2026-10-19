from pathlib import Path

for f in Path("md").glob("*.md"):
	Path(f"html/{f.stem}.html").write_text(
		Path("template.html").read_text().replace(
			"<body></body>",
			"\n".join([
				"<body>",
				*f.read_text().splitlines(),
				"</body>"
			])
		)
	)
