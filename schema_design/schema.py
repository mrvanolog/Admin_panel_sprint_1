import psycopg2

conn = psycopg2.connect(
    dbname='movies',
    user='mrvanolog',
    host='localhost',
    port=5432,
    options='-c search_path=content',
)

cur = conn.cursor()

sql_schema = """
-- Создаем отдельную схему для нашего контента, чтобы не перемешалось с сущностями Django
CREATE SCHEMA IF NOT EXISTS content;

-- Убраны актеры, жанры, режиссеры и сценаристы, так как они находятся в отношении m2m с таблицей
CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    certificate TEXT,
    file_path TEXT,
    rating FLOAT,
    type TEXT not null,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Жанры, которые могут быть у кинопроизведений
CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Таблица с информацией о сценаристе
CREATE TABLE IF NOT EXISTS content.writer (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    birth_date DATE,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Таблица с информацией об актере
CREATE TABLE IF NOT EXISTS content.actor (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    birth_date DATE,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Таблица с информацией о режиссере
CREATE TABLE IF NOT EXISTS content.director (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    birth_date DATE,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- m2m таблица для связывания кинопроизведений с жанрами
CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    genre_id uuid NOT NULL,
    created_at timestamp with time zone
);

-- m2m таблица для связывания кинопроизведений со сценаристом
CREATE TABLE IF NOT EXISTS content.writer_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    writer_id uuid NOT NULL,
    created_at timestamp with time zone
);

-- m2m таблица для связывания кинопроизведений с актером
CREATE TABLE IF NOT EXISTS content.actor_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    actor_id uuid NOT NULL,
    created_at timestamp with time zone
);

-- m2m таблица для связывания кинопроизведений с режиссером
CREATE TABLE IF NOT EXISTS content.director_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    director_id uuid NOT NULL,
    created_at timestamp with time zone
);

-- Обязательно проверяется уникальность жанра и кинопроизведения, чтобы не появлялось дублей
CREATE UNIQUE INDEX film_work_genre ON content.genre_film_work (film_work_id, genre_id);

-- Обязательно проверяется уникальность кинопроизведения и сценариста, чтобы не появлялось дублей
CREATE UNIQUE INDEX film_work_writer ON content.writer_film_work (film_work_id, writer_id);

-- Обязательно проверяется уникальность кинопроизведения и акетра, чтобы не появлялось дублей
CREATE UNIQUE INDEX film_work_actor ON content.actor_film_work (film_work_id, actor_id);

-- Обязательно проверяется уникальность кинопроизведения и режиссера, чтобы не появлялось дублей
CREATE UNIQUE INDEX film_work_director ON content.director_film_work (film_work_id, director_id);
"""

cur.execute(sql_schema)

conn.commit()
cur.close()
conn.close()
