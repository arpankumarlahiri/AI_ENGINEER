.PHONY: sync test serve lint fmt docker


PORT ?= 8080

sync:
	uv sync

test:
	uv run pytest

serve:
	uv run uvicorn src.ai_engineer.app:app --reload --port $(PORT)

docker:
	docker build -t ai-engineer .
	docker run --rm -p $(PORT):8080 --env-file .env  ai-engineer

lint:
	uv run ruff check .

fmt:
	uv run ruff format .
	uv run ruff check --fix .
