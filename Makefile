.SILENT:
.PHONY: all preview

all:
	uv run --with jinja2 --with python-frontmatter python -B build.py

preview: all
	python -m http.server --directory _site
