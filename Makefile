.ONESHELL:
.SILENT:
.PHONY: all cv posts preview

all: cv posts

cv:
	npx md-to-pdf cv.md --stylesheet cv.css

posts:
	rm -rf _site
	uv run --with jinja2 --with python-frontmatter python -B build.py

preview:
	npx browser-sync start --server _site --files "_site/**/*" --no-ui &
	pid=$$!
	trap "test -n '$${pid}' && kill '$${pid}'" EXIT INT TERM
	npx chokidar-cli build.py config.toml template.css template.xml "posts/**/*.md" \
		-c "$(MAKE) $(filter-out preview,$(MAKECMDGOALS))"
