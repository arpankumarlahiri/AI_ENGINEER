.PHONY: sync test serve lint fmt


PORT ?= 8080

sync:
	uv sync

test:
	uv run pytest

serve:
	uv run uvicorn src.ai_engineer.app:app --reload --port $(PORT)

lint:
	uv run ruff check .

fmt:
	uv run ruff format .
	uv run ruff check --fix .