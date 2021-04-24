.PHONY: test

deps:
	pip install -r requirements.txt; \
	pip install -r test-requirements.txt

test:
	PYTHONPATH=. py.test --verbose -s
