import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop  = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop       = "DROP TABLE IF EXISTS songplays"
user_table_drop           = "DROP TABLE IF EXISTS users"
song_table_drop           = "DROP TABLE IF EXISTS songs"
artist_table_drop         = "DROP TABLE IF EXISTS artists"
time_table_drop           = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""CREATE TABLE IF NOT EXISTS staging_events (
                                 artist VARCHAR,
                                 auth VARCHAR,
                                 firstName VARCHAR,
                                 gender CHAR,
                                 itemInSession INTEGER,
                                 lastName VARCHAR,
                                 length FLOAT,
                                 level VARCHAR,
                                 location VARCHAR,
                                 method VARCHAR,
                                 page VARCHAR,
                                 registration DOUBLE PRECISION,
                                 sessionId INTEGER,
                                 song VARCHAR,
                                 status INTEGER,
                                 ts BIGINT,
                                 userAgent VARCHAR,
                                 userId VARCHAR);
                                 """)

staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS staging_songs (
                                 num_songs INT NOT NULL PRIMARY KEY,
                                 artist_id CHAR(18),
                                 artist_latitude FLOAT,
                                 artist_longitude FLOAT,
                                 artist_location VARCHAR,
                                 artist_name VARCHAR,
                                 song_id CHAR(18) NOT NULL,
                                 title VARCHAR,
                                 duration FLOAT NOT NULL,
                                 year INT);
                                 """)

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                            songplay_id INT IDENTITY(0,1) PRIMARY KEY,
                            start_time BIGINT,
                            user_id VARCHAR,
                            level VARCHAR,
                            song_id CHAR(18) NOT NULL,
                            artist_id CHAR(18),
                            session_id INT NOT NULL,
                            location VARCHAR,
                            user_agent VARCHAR);
                            """)

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                        user_id VARCHAR PRIMARY KEY,
                        first_name VARCHAR,
                        last_name VARCHAR,
                        gender CHAR,
                        level VARCHAR);
                        """)

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                        song_id CHAR(18) NOT NULL PRIMARY KEY, 
                        title TEXT NOT NULL,
                        artist_id CHAR(18),
                        year INT,
                        duration FLOAT NOT NULL);
                        """)

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                          artist_id CHAR(18) NOT NULL PRIMARY KEY,
                          name TEXT NOT NULL,
                          location VARCHAR,
                          latitude FLOAT,
                          longitude FLOAT);
                          """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                            start_time BIGINT NOT NULL PRIMARY KEY,
                            hour INT,
                            day INT,
                            week INT,
                            month INT,
                            year INT,
                            weekday INT);
                            """)

# STAGING TABLES

staging_events_copy = ("""COPY staging_events
                          FROM {}
                          iam_role {}
                          FORMAT as JSON 'auto ignorecase';
                          """).format(config['S3']['LOG_DATA'],
                                      config['IAM_ROLE']['ARN'])

staging_songs_copy = ("""COPY staging_songs
                          FROM {}
                          iam_role {}
                          FORMAT as JSON 'auto ignorecase';
                          """).format(config['S3']['SONG_DATA'],
                                      config['IAM_ROLE']['ARN'])

# FINAL TABLES

songplay_table_insert = ("""INSERT INTO songplays (
                                start_time,
                                user_id,
                                level,
                                song_id,
                                artist_id,
                                session_id,
                                location,
                                user_agent)
                            SELECT e.ts,
                                e.userId,
                                e.level,
                                s.song_id,
                                s.artist_id,
                                e.sessionId,
                                e.location,
                                e.userAgent
                            FROM staging_events e, staging_songs s
                            WHERE (s.title = e.song) AND (s.artist_name = e.artist);
                            """)

user_table_insert     = ("""INSERT INTO users (
                                user_id,
                                first_name,
                                last_name,
                                gender,
                                level)
                            SELECT DISTINCT userId,
                                firstName,
                                lastName,
                                gender,
                                level
                            FROM staging_events
                            WHERE userId IS NOT NULL;
                            """)

song_table_insert     = ("""INSERT INTO songs (
                                song_id,
                                title,
                                artist_id,
                                year,
                                duration)
                            SELECT DISTINCT song_id,
                                title,
                                artist_id,
                                year,
                                duration
                            FROM staging_songs;
                            """)

artist_table_insert   = ("""INSERT INTO artists (
                                artist_id,
                                name,
                                location,
                                latitude,
                                longitude)
                            SELECT DISTINCT s.artist_id,
                                s.artist_name,
                                e.location,
                                s.artist_latitude,
                                s.artist_longitude
                            FROM staging_events e, staging_songs s
                            WHERE (e.artist=s.artist_name) AND (e.song=s.title);
                            """)

time_table_insert     = ("""INSERT INTO time (
                            start_time,
                            hour,
                            day,
                            week,
                            month,
                            year,
                            weekday)
                         SELECT DISTINCT ts,
                            EXTRACT('hour' FROM to_timestamp ( ts::bigint::text,'YYYYMMDDHH')::timestamp at time zone 'UTC'),
                            EXTRACT('day' FROM to_timestamp ( ts::bigint::text,'YYYYMMDDHH')::timestamp at time zone 'UTC'),  
                            EXTRACT('week' FROM to_timestamp ( ts::bigint::text,'YYYYMMDDHH')::timestamp at time zone 'UTC'), 
                            EXTRACT('month' FROM to_timestamp ( ts::bigint::text,'YYYYMMDDHH')::timestamp at time zone 'UTC'), 
                            EXTRACT('year' FROM to_timestamp ( ts::bigint::text,'YYYYMMDDHH')::timestamp at time zone 'UTC'),  
                            EXTRACT('dayofweek' FROM to_timestamp ( ts::bigint::text,'YYYYMMDDHH')::timestamp at time zone 'UTC')
                         FROM staging_events
                         WHERE ts IS NOT NULL;
                         """)

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
