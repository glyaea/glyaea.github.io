.SILENT:
.PHONY: all

all:
	uv run --with jinja2 python -B build.py
	open http://localhost:8000 &
	python -m http.server --directory _site
