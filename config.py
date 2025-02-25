import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="testapi",
        user="postgres",
        password="1017",
        host="localhost",
        port="5432"
    )
    return conn