from user import User
from activity import Activity
from backup import export_to_json, import_from_json

def main_menu():
    print("Welcome to the Health Tracker!")
    logged_in_user = None  # Track the logged-in user

    while True:
        if not logged_in_user:
            print("\nMain Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = User(username, password)
                user.register()

            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = User(username, password)
                if user.login():
                    print("Login successful.")
                    logged_in_user = user  # Set logged-in user
                else:
                    print("Login failed.")
            
            elif choice == '3':
                print("Exiting the application.")
                break

            else:
                print("Invalid choice. Please try again.")

        else:
            print("\nUser Menu:")
            print("1. Log Activity")
            print("2. View Activities")
            print("3. Export Data to JSON")
            print("4. Import Data from JSON")
            print("5. Logout")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                steps = int(input("Enter steps: "))
                calories = int(input("Enter calories burned: "))
                active_minutes = int(input("Enter active minutes: "))
                water_ml = int(input("Enter water intake (ml): "))
                activity = Activity(logged_in_user.user_id, steps, calories, active_minutes, water_ml)
                activity.log_activity()

            elif choice == '2':
                # Obtener todas las actividades del usuario logueado
                activities = Activity.get_all_activities(logged_in_user.user_id)
                if activities:
                    for act in activities:
                        print(f"Date: {act[2]}, Steps: {act[3]}, Calories: {act[4]}, Active Minutes: {act[5]}, Water: {act[6]} ml")
                else:
                    print("No activities found.")

            elif choice == '3':
                filename = input("Enter filename for export: ")
                export_to_json(filename)

            elif choice == '4':
                filename = input("Enter filename for import: ")
                import_from_json(filename)

            elif choice == '5':
                logged_in_user = None  # Log out user
                print("Logged out successfully.")

            elif choice == '6':
                print("Exiting the application.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()