insert_movie = ('''
    TODO
''')

create_schema = ('''
CREATE SCHEMA IF NOT EXISTS petl2
''')

drop_table = ('''
DROP TABLE IF EXISTS petl2.movie_list
''')

create_table = ('''
CREATE TABLE IF NOT EXISTS petl2.movie_list (
title TEXT NOT NULL,
rated TEXT NOT NULL,
released DATE NOT NULL,
runtime INTEGER NOT NULL,
genre TEXT[] NOT NULL,
director TEXT NOT NULL,
writers TEXT[] NOT NULL,
actors TEXT[] NOT NULL,
plot TEXT NOT NULL,
awards TEXT NOT NULL,
poster TEXT NOT NULL
)
''')

insert_data = ('''
INSERT INTO petl2.movie_list
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
''')
