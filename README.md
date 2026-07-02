# UniMaaS Core Integration Platform

FastAPI backend-for-frontend for IC17, the UniMaaS Core Integration Platform.

Keep `pyproject.toml` and `uv.lock` tracked. Docker uses them for reproducible production dependency installs.

## Run With Docker Compose

```bash
cp .env.example .env
docker compose up --build
```

Open:

- Swagger UI: <http://127.0.0.1:8000/docs>
- Health check: <http://127.0.0.1:8000/health>

```bash
docker compose down
```

## Optional Local Development

```bash
uv sync --dev
uv run uvicorn app.main:app --reload
```

Open:

- Swagger UI: <http://127.0.0.1:8000/docs>
- OpenAPI JSON: <http://127.0.0.1:8000/openapi.json>

## API Grouping

Swagger tags are grouped by downstream component:

- `ic1-edc-connector`
- `ic3-knowledge-graph`
- `ic4-federated-catalogue`
- `ic5-resource-monitoring`
- `ic6-iam-data-governance`
- `ic7-dpp-infrastructure`
- `ic11-intent-chatbot`
- `ic15-cloud-mfg-orchestrator`

Blocked integrations return `501 Not Implemented` with the missing inputs.

## App Structure

- `app/main.py`: FastAPI app creation and router registration.
- `app/routers/`: HTTP endpoints grouped by downstream component.
- `app/services/`: integration behavior grouped by downstream component.
- `app/clients/`: future outbound clients.
- `app/schemas/`: Pydantic request and response models.
- `app/settings.py`: environment variable loading.

## Integration Tracking

The integration tracking file is `docs/integration.md`.

## Tests

```bash
uv run pytest
```
