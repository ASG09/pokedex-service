run:
	python3 -m src.main

test:
	pytest src/tests/

lint:
	flake8 src/ --select=WPS