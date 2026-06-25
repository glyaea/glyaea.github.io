.ONESHELL:
.SILENT:
.PHONY: all cv preview

all:
	uv run --with jinja2 --with python-frontmatter python -B build.py

cv:
	npx md-to-pdf cv.md \
		--stylesheet cv.css \
		--body-class markdown-body \
		--pdf-options '{"format":"A4","margin":"1.61803398875cm"}'

preview: all
	npx browser-sync start --server _site --files "_site/**/*" --no-ui &
	pid=$$!
	trap "test -n '$${pid}' && kill '$${pid}'" EXIT INT TERM
	npx chokidar-cli build.py config.toml index.css template.html "posts/**/*.md" -c make
