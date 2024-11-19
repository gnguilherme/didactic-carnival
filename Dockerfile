FROM python:3.10-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY ./app /app
COPY ./pyproject.toml ./uv.lock ./README.md gradio_app.py ./

RUN uv sync --frozen

ENTRYPOINT ["uv", "run"]