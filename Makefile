.DEFAULT_GOAL = yapf-lint

.PHONY: yapf-lint
yapf-lint:
	# check for violation of code against YAPF formatting convention
	yapf --style pep8 --no-local-style --verbose --recursive --diff --parallel ./my_telegram_bot ./tests

.PHONY: yapf-format
yapf-format:
	# modify code to fit YAPF formatting convention
	yapf --style pep8 --no-local-style --verbose --recursive --parallel --in-place ./my_telegram_bot ./tests

.PHONY: pyflakes
pyflakes:
	pyflakes ./my_telegram_bot ./tests