from fastapi import FastAPI

app = FastAPI(title="prova1-fastapi")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI is working"}


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
