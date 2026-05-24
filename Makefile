.PHONY: all FORCE

all: index.html

index.html: FORCE index.py posts/*.md
	python -B index.py

FORCE:
