import socket
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/info")
def root() -> dict[str,str]:
    return {
        "message": "FastAPI is running",
        "datetime": datetime.now(timezone.utc).isoformat(),
        "hostname": socket.gethostname(),
    }

@app.get("/api/v1/health")
def health() -> dict[str,str]:
    return {"status": "ok"}


