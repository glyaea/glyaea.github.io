.ONESHELL:
.SILENT:
.PHONY: all preview

all:
	uv run --with jinja2 --with python-frontmatter python -B build.py

preview: all
	npx browser-sync start --server _site --files "_site/**/*" --no-ui &
	pid=$$!
	trap "test -n '$${pid}' && kill '$${pid}'" EXIT INT TERM
	npx chokidar-cli build.py config.toml index.css template.html "posts/**/*.md" -c make
