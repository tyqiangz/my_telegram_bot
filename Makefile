.DEFAULT_GOAL = lint

.PHONY: yapf-lint
yapf-lint:
	yapf --style '{based_on_style: pep8, dedent_closing_brackets: true, coalesce_brackets: true}' \
		 --no-local-style --verbose --recursive --diff --parallel .

.PHONY: yapf-format
yapf-format:
	yapf --style '{based_on_style: pep8, dedent_closing_brackets: true, coalesce_brackets: true}' \
		 --no-local-style --verbose --recursive --in-place --parallel .