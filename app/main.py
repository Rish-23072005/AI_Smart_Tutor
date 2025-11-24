from __future__ import annotations

import os
import subprocess
import threading
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.endpoints import ask, progress, quiz

settings = get_settings()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ask.router, prefix="/ask", tags=["Ask"])
app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])
app.include_router(progress.router, prefix="/progress", tags=["Progress"])


def _run_streamlit() -> None:
    streamlit_script = Path(__file__).parent / "frontend" / "app.py"
    command = [
        "streamlit",
        "run",
        str(streamlit_script),
        "--server.port",
        str(settings.streamlit_port),
        "--server.address",
        settings.api_host,
    ]
    subprocess.Popen(command)  # noqa: S603,S607


if os.getenv("START_STREAMLIT", "false").lower() == "true":
    threading.Thread(target=_run_streamlit, daemon=True).start()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True,
    )

