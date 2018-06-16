test: test_lint test_unit

test_unit:
	pytest tests/unit

test_lint:
	flake8

test_mypy:
	mypy --py2 awspricing
