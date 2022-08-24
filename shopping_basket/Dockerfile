FROM python:3.9.13-slim-buster

RUN apt update; apt install make
WORKDIR /app

COPY app.py /app/app.py
COPY shopping_basket /app/shopping_basket
COPY tests /app/tests
COPY Makefile /app/Makefile
COPY poetry.lock /app/poetry.lock
COPY pyproject.toml /app/pyproject.toml
COPY README.md /app/README.md
COPY mypy.ini /app
COPY .flake8 /app
COPY .editorconfig /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN make

CMD python -m unittest discover .
