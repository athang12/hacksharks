import schedule
import time

def function1():
    print("Function 1 executed")

def function2():
    # Counter to keep track of the number of executions
    counter = 0

    while counter < 5:
        print("Function 2 executed")
        counter += 1
        time.sleep(5)  # Wait for 10 minutes between each execution

# Schedule function1 to run every Monday at 9:00 AM
schedule.every().saturday.at("03:44").do(function1)

# Schedule function2 to run every Wednesday at 2:30 PM
schedule.every().saturday.at("03:44").do(function2)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    if not schedule.jobs:  # Check if there are any scheduled jobs
        break  # Exit the loop if no more jobs are scheduled
    time.sleep(1)