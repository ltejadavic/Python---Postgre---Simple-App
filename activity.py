from database import connect
from datetime import date

class Activity:
    def __init__(self, user_id, steps=0, calories=0, active_minutes=0, water_ml=0):
        self.user_id = user_id
        self.date = date.today()
        self.steps = steps
        self.calories = calories
        self.active_minutes = active_minutes
        self.water_ml = water_ml

    def log_activity(self):
        conn = connect()
        cur = conn.cursor()
        try:
            cur.execute("""
            INSERT INTO activities (user_id, date, steps, calories, active_minutes, water_ml) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (self.user_id, self.date, self.steps, self.calories, self.active_minutes, self.water_ml))
            conn.commit()
            print("Activity logged successfully.")
        except Exception as e:
            print(f"Error logging activity: {e}")
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def get_all_activities(user_id):
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
        SELECT * FROM activities WHERE user_id = %s ORDER BY date DESC
        """, (user_id,))
        activities = cur.fetchall()
        cur.close()
        conn.close()
        return activities