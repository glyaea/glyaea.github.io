all:
	cd posts && python3 build.py

preview: all
	python3 -m http.server 8000
