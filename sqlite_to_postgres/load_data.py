import psycopg2
import sqlite3
from psycopg2.extensions import connection as _connection
from pathlib import Path

from utils.sqliteloader import SQLiteLoader
from utils.postgressaver import PostgresSaver


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_loader = SQLiteLoader(connection)

    data = sqlite_loader.load_movies()
    postgres_saver.save_all_data(data)


if __name__ == "__main__":
    sqlite_path = Path(__file__).parent.joinpath("db.sqlite")
    dsl = {
        "dbname": "movies",
        "user": "postgres",
        "password": 123,
        "host": "127.0.0.1",
        "port": 5432,
    }
    with sqlite3.connect(sqlite_path) as sqlite_conn, psycopg2.connect(**dsl) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
