import psycopg2

def connect():
    return psycopg2.connect(
        dbname="health_tracker",
        user="postgres",
        password="Marvin1926",
        host="localhost",
        port="5432"
    )

def create_tables():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL
    );
    
    CREATE TABLE IF NOT EXISTS activities (
        activity_id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(user_id),
        date DATE NOT NULL,
        steps INT,
        calories INT,
        active_minutes INT,
        water_ml INT
    );
    """)
    conn.commit()
    cur.close()
    conn.close()