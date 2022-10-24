
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id serial PRIMARY KEY,
    start_time timestamp NOT NULL,
    user_id int NOT NULL,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id int NOT NULL,
    location varchar,
    user_agent varchar
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id int PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY,
    title varchar,
    artist_id varchar NOT NULL,
    year int,
    duration numeric
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar PRIMARY KEY,
    name varchar,
    location varchar,
    latitude numeric,
    longitude numeric
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time timestamp PRIMARY KEY,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
);
""")

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]