# bash needed for pipefail
SHELL := /bin/bash

test: test_lint test_unit

test_unit:
	py.test tests/unit

test_lint:
	flake8

test_mypy:
	mypy --py2 awspricing
