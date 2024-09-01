from database import connect

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_id = None  # Initialize user_id

    def register(self):
        conn = connect()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (self.username, self.password))
            conn.commit()
            print(f"User {self.username} registered successfully.")
        except Exception as e:
            print(f"Error registering user: {e}")
        finally:
            cur.close()
            conn.close()

    def login(self):
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM users WHERE username = %s AND password = %s", (self.username, self.password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            self.user_id = user[0]  # Set user_id if login is successful
            return True
        return False