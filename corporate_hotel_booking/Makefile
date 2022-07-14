.PHONY: all clean lint type test test-cov

CMD := poetry run
PYMODULE := corportate_hotel_booking
EXTRACODE :=

all: poetry-install mypy-install-types type lint format-check
format: black isort
format-check: black-check isort-check

poetry-install:
	poetry install

mypy-install-types:
	$(CMD) mypy --install-types --non-interactive --follow-imports=skip $(PYMODULE)

lint:
	$(CMD) flake8 $(PYMODULE) $(EXTRACODE)

type:
	$(CMD) mypy --follow-imports=skip $(PYMODULE) $(EXTRACODE)

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
