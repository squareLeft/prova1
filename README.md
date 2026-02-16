# FastAPI Base Project

Struttura base di un progetto **FastAPI** con:
- containerizzazione tramite **Docker**
- test con **pytest** organizzati in cartelle separate (`tests/unit` e `tests/integration`)

## Struttura progetto

```text
.
├── app/
│   ├── api/
│   │   └── routes.py
│   └── main.py
├── tests/
│   ├── integration/
│   │   └── test_root.py
│   └── unit/
│       └── test_health.py
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── requirements.txt
└── requirements-dev.txt
```

## Avvio locale

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

API disponibile su `http://127.0.0.1:8000`.

## Avvio con Docker

```bash
docker compose up --build
```

API disponibile su `http://127.0.0.1:8000`.

## Esecuzione test

```bash
pytest
```
