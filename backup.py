import json
from database import connect
from datetime import date

def export_to_json(filename):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM activities")
    activities = cur.fetchall()
    cur.close()
    conn.close()

    # Convert date objects to strings
    activities_list = []
    for activity in activities:
        activity_dict = {
            "activity_id": activity[0],
            "user_id": activity[1],
            "date": activity[2].strftime('%Y-%m-%d'),
            "steps": activity[3],
            "calories": activity[4],
            "active_minutes": activity[5],
            "water_ml": activity[6]
        }
        activities_list.append(activity_dict)

    with open(filename + '.json', 'w') as f:
        json.dump(activities_list, f)

    print(f"Data exported to {filename}.json.")

def import_from_json(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, 'r') as f:
        activities = json.load(f)
        for activity in activities:
            cur.execute("""
            INSERT INTO activities (activity_id, user_id, date, steps, calories, active_minutes, water_ml) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, activity)
    conn.commit()
    cur.close()
    conn.close()
    print(f"Data imported from {filename}.")