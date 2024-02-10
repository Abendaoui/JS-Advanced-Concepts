from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format the current date to get the day of the week
current_day_of_week = current_datetime.strftime("%A")

print("Current Day of the Week:", current_day_of_week)
