import time
import os
from plyer import notification

def send_notification():
    notification.notify(
        title="Drink Water Reminder",
        message="Time to drink water! Stay hydrated!",
        app_name="Water Reminder",
        timeout=10
    )

def main():
    interval = 60 * 60  # Remind every hour
    while True:
        send_notification()
        time.sleep(interval)

if __name__ == "__main__":
    main()
