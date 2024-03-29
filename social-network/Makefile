.PHONY: all clean lint type test test-cov

CMD := poetry run
PYMODULE := src
EXTRACODE :=

all: poetry-install mypy lint format-check tests
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
	$(CMD) isort --check $(PYMODULE) $(EXTRACODE)

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
	docker build -t social-network-api .

test:
	poetry run pytest
