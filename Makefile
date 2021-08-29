.PHONY: check format tests

install-ubuntu:
	rm -r venv
	python3.9 -m venv venv
	( \
		. venv/bin/activate && \
		which pip; \
		python3.9 -m pip install --upgrade pip && \
		pip install flake8 pytest black \
	)

check:
	black --check --line-length 100 exercise.py
	black --check --line-length 100 tests.py
	flake8 --max-line-length 100 exercise.py
	flake8 --max-line-length 100 tests.py

format:
	black --line-length 100 exercise.py
	black --line-length 100 tests.py

tests:
	pytest tests.py -vv