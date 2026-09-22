import os
import sqlite3
from pathlib import Path

from config import SQLITE_DB_PATH

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


if load_dotenv is not None:
    backend_dir = Path(__file__).resolve().parent
    load_dotenv(backend_dir / ".env")
    load_dotenv(backend_dir.parent / ".env")


def has_turso_credentials():
    

    return bool(os.getenv("TURSO_DATABASE_URL") and os.getenv("TURSO_AUTH_TOKEN"))


def connect_database():
    

    if has_turso_credentials():
        import turso_serverless

        return turso_serverless.connect(
            os.environ["TURSO_DATABASE_URL"],
            auth_token=os.environ["TURSO_AUTH_TOKEN"],
        )

    return sqlite3.connect(SQLITE_DB_PATH)


def database_row_factory():
    

    if has_turso_credentials():
        from turso_serverless.connection import Row

        return Row

    return sqlite3.Row


def initialize_database():
    

    with connect_database() as connection:
        connection.executescript(
            
        )


def add_document(file_name, law_name, source, document_version):
    

    with connect_database() as connection:
        cursor = connection.execute(
            ,
            (file_name, law_name, source, document_version),
        )
        document_id = cursor.lastrowid
        cursor.close()

    return document_id


def add_chunk(
    document_id,
    chunk_id,
    law_name,
    section_name,
    page_number,
    chunk_text,
):
    

    with connect_database() as connection:
        connection.execute(
            ,
            (
                chunk_id,
                document_id,
                law_name,
                section_name,
                page_number,
                chunk_text,
            ),
        )


def get_all_chunks():
    

    if not has_turso_credentials() and not SQLITE_DB_PATH.exists():
        return []

    with connect_database() as connection:
        connection.row_factory = database_row_factory()

        table_exists = connection.execute(
            
        ).fetchone()

        if table_exists is None:
            return []

        rows = connection.execute(
            
        ).fetchall()

    return rows
