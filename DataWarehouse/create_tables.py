import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drop tables in database.
    
    Keyword arguments:
    cur - cursor to execute SQL command in a database session 
    conn -  connection to the database
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create tables in database.
    
    Keyword arguments:
    cur - cursor to execute SQL command in a database session 
    conn -  connection to the database
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Establishing a connection to the database, dropping previous and creating new tables.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()