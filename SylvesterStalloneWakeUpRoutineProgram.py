import sqlite3
import time

# Create a SQLite database and connect to it
dbfile = 'daily_stats.db'
conn = sqlite3.connect(dbfile)
cursor = conn.cursor()

# Create a table to store daily stats if it doesn't exist
create_table_sql = '''
CREATE TABLE IF NOT EXISTS daily_stats (
    id INTEGER PRIMARY KEY,
    date TEXT,
    sleep_duration REAL,
    exercise_done TEXT,
    breakfast_done TEXT,
    shower_done TEXT,
    clothes_prepared TEXT,
    lunch_prepared TEXT
)
'''
cursor.execute(create_table_sql)
conn.commit()

# Sylvester Stallone-style prompts
def sylvester_speak(message):
    print(f"Sylvester Stallone: {message}")

# Check if the user has reported for the last 5 days
def check_consecutive_days_reported():
    cursor.execute("SELECT date FROM daily_stats ORDER BY date DESC LIMIT 5")
    last_five_dates = [row[0] for row in cursor.fetchall()]

    if len(last_five_dates) == 5:
        current_date = time.strftime('%Y-%m-%d')
        expected_date = (time.strftime('%Y-%m-%d', time.gmtime(time.mktime(time.strptime(current_date, '%Y-%m-%d')) - 86400)))

        # Check if the user reported consecutively for the last 5 days
        if expected_date in last_five_dates:
            sylvester_speak("That's five days in a row! You're on fire, kid!")
            sylvester_speak("Keep up the good work!")

# Get bedtime and wake-up time from the user in military time
sylvester_speak("What time did you go to bed (HH:MM)?")
bedtime_str = input()
sylvester_speak("What time did you wake up (HH:MM)?")
wakeup_time_str = input()

# Convert bedtime and wake-up time to Time::Piece objects
bedtime = time.strptime(bedtime_str, '%H:%M')
wakeup_time = time.strptime(wakeup_time_str, '%H:%M')

# Calculate the approximate number of hours of sleep
sleep_duration = (24 - bedtime.tm_hour) + wakeup_time.tm_hour + (wakeup_time.tm_min - bedtime.tm_min) / 60

# Determine if it's good or bad sleep duration
if sleep_duration >= 7:
    feedback = "That's a good amount of sleep!"
elif sleep_duration >= 6:
    feedback = "You got a decent amount of sleep."
else:
    feedback = "You may need more sleep for optimal health"

# Print the results
print(f"Sylvester Stallone: You slept for approximately {sleep_duration:.2f} hours.")
sylvester_speak(feedback)

# Sleep for 2 seconds
time.sleep(2)

# Prompt the user to do exercises
sylvester_speak("Hey, it's time to get moving! I want you to do 10 pushups, 10 sit-ups, and 10 jumping jacks. Go and say 'OK' when you're done!")
response = input()
if response.lower() == 'ok':
    sylvester_speak("Good job! Now, it's time to fuel up with a healthy breakfast. Make sure to include some proteins and fruits. Say 'OK' when you're ready!")
else:
    sylvester_speak("Come on! Get it done!")

# Wait for the breakfast OK
response = input()
if response.lower() == 'ok':
    sylvester_speak("Great! Now, take a quick shower, and I mean quick! Report back immediately with another 'OK'.")
else:
    sylvester_speak("No excuses! Get that breakfast and get moving!")

# Wait for the shower OK
response = input()
sylvester_speak("Now, did you prepare your clothes for today from last night? (yes sir / no sir)")
clothes_response = input()
if clothes_response.lower() == 'no sir':
    sylvester_speak("Unbelievable! Being disorganized is a recipe for disaster.")

sylvester_speak("Now, did you prepare your lunch for today from last night? (yes sir / no sir)")
lunch_response = input()
if lunch_response.lower() == 'no sir':
    sylvester_speak("You gotta be prepared, kid. Being disorganized is not the way to go!")

# Provide a summary report
sylvester_speak("Alright, here's your summary for the day:")
sylvester_speak(f"Sleep duration: {sleep_duration:.2f} hours")
sylvester_speak(f"Exercise done: {response.lower()}")
sylvester_speak(f"Breakfast done: {response.lower()}")
sylvester_speak(f"Shower done: {response.lower()}")
sylvester_speak(f"Clothes prepared: {clothes_response.lower()}")
sylvester_speak(f"Lunch prepared: {lunch_response.lower()}")

sylvester_speak("Now, it's time to get to work on time. Go and give it your all!")

# Close the database connection
conn.close()
