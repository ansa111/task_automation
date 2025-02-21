import schedule
import time
from automation.email_sender import send_email
from automation.notifier import send_notification

def job():
    print("Executing scheduled task...")
    send_email("test@example.com", "Scheduled Email", "This is an automated email.")
    send_notification("This is a scheduled notification!")

def start_scheduler():
    schedule.every(10).seconds.do(job)  # Runs every 10 seconds for testing

    while True:
        schedule.run_pending()
        time.sleep(1)
