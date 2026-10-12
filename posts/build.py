from pathlib import Path

for f in Path("md").glob("*.md"):
	Path(f"html/{f.stem}.html").write_text(
		Path("template.html").read_text().replace(
			"<body></body>",
			f"<body>\n{f.read_text().rstrip('\n')}\n</body>"
		)
	)
