FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY linkedin_simulator/ ./linkedin_simulator/

ENTRYPOINT ["python", "-m", "linkedin_simulator.main"]