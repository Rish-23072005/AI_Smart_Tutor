from __future__ import annotations

from pathlib import Path


def ingest_pdf(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(file_path)
    # Placeholder for real ingestion logic
    return f"Ingested {path.name} into vector store"

