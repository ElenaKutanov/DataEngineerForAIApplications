### The project for extracting data from S3, stages them in Redshift and transform data into a set of dimetional tables for the Sparkify analitics team.

#### Files:
- create_tables.py - for creating and dropping tabels in database.
- dwh.cfg is a configuration file with acsses data for Redshift cluster, S3 and iam role.
- etl.py - ETL piplene for loading data from S3 and inserting into stages and dimentional tables.
- sql_queries.py includes all queries for creating/dropping tables and loading/inserting data into the database.

To run the project, start "python create_tables.py" in terminal for creating the database and then "python etl.py" to load the data.

The Redshift database includes staging tables to save the data from json files on S3:
- staging_events
- staging_songs
and dimensional tables to prepare the data for the analytical goals:
- songplays
- users
- songs
- artists
- time
There is a fact table playsongs, which is used by the analytics team to continue finding insights into what songs users are listening to. And dimensional tables to store the data about songs, users, artists and timestamps. 

![alt text](https://github.com/ElenaKutanov/de_nd/blob/main/db.png)
