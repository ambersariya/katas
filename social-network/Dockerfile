FROM python:3.11-slim

RUN apt update; apt install make
WORKDIR /app

COPY src /app/src
COPY pyproject.toml /app
COPY poetry.lock /app
COPY README.md /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000
CMD ["uvicorn", "src.web.app:app", "--host", "0.0.0.0", "--port", "8000"]
