all:
	echo -n 'var unicode = ' > unicode.js
	python u.py >> unicode.js

.PHONY: all

