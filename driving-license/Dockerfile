FROM python:3.10.8-slim-bullseye

WORKDIR /app

COPY driving_license /app/driving_license
COPY app.py /app/app.py
COPY poetry.lock /app/poetry.lock
COPY pyproject.toml /app/pyproject.toml

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000
CMD ["uvicorn", "app:driving_license_app", "--host", "0.0.0.0", "--port", "8000"]
