.DEFAULT_GOAL = lint

.PHONY: yapf-lint
yapf-lint:
	yapf --style pep8 --no-local-style --verbose --recursive --diff --parallel .

.PHONY: yapf-format
yapf-format:
	yapf --style pep8 --no-local-style --verbose --recursive --parallel --in-place .