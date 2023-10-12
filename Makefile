.DEFAULT_GOAL = lint

.PHONY: yapf-lint
yapf-lint:
	# check for violation of code against YAPF formatting convention
	yapf --style pep8 --no-local-style --verbose --recursive --diff --parallel ./src ./tests

.PHONY: yapf-format
yapf-format:
	# modify code to fit YAPF formatting convention
	yapf --style pep8 --no-local-style --verbose --recursive --parallel --in-place ./src ./tests

.PHONY: pyflakes
pyflakes:
	pyflakes ./src ./tests