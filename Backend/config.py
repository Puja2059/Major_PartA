from pathlib import Path
import os


CHROMA_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = CHROMA_DIR.parent

DATA_DIR = CHROMA_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

LEGAL_DOCUMENTS_DIR = CHROMA_DIR / "legal_documents"
LEGAL_DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)

CHROMA_DB_PATH = CHROMA_DIR / "chroma_db"
CHROMA_DB_PATH.mkdir(parents=True, exist_ok=True)

SQLITE_DB_PATH = DATA_DIR / "legal_metadata.db"

CHROMA_COLLECTION_NAME = "nepal_legal_documents"


EMBEDDING_MODEL_NAME = (
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

VECTOR_TOP_K = 8
BM25_TOP_K = 8

FINAL_TOP_K = 5

EXTERNAL_SEARCH_ENABLED = True
EXTERNAL_SEARCH_TOP_K = 5
VECTOR_MATCH_DISTANCE_THRESHOLD = 0.8
