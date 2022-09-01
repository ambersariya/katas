.PHONY: all clean lint type test test-cov

CMD := poetry run
PYMODULE := shopping_basket
EXTRACODE :=

all: poetry-install mypy lint format-check
format: black isort
format-check: black-check isort-check

poetry-install:
	poetry install --no-interaction --no-ansi

mypy:
	$(CMD) mypy --install-types --non-interactive --follow-imports=skip -p $(PYMODULE)

lint:
	$(CMD) flake8 $(PYMODULE) $(EXTRACODE)

isort:
	$(CMD) isort $(PYMODULE) $(EXTRACODE)

isort-check:
	$(CMD) isort --check --verbose $(PYMODULE) $(EXTRACODE)

clean:
	git clean -Xdf # Delete all files in .gitignore

black:
	$(CMD) black .

black-check:
	$(CMD) black --check .

update-libs: # Updates python dependencies and commits
	poetry update
	git add poetry.lock && git commit poetry.lock -m "chore: update project dependencies"

build-image:
	docker build -t shopping-basket-api .
