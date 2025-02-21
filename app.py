from flask import Flask
from flask_mail import Mail, Message
import schedule
import time
import threading

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com' # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_email_password'    # Replace with your password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

mail = Mail(app)

# Flask route
@app.route('/')
def home():
    return "Hello, Flask with Email Notifications!"

# Function to send an email
def send_email():
    try:
        msg = Message('Scheduled Notification', recipients=['recipient@example.com'])
        msg.body = 'This is an automated email sent by the Flask app.'
        mail.send(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the task every 10 seconds
schedule.every(10).seconds.do(send_email)

# Function to run schedule in a separate thread
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduling thread
thread = threading.Thread(target=run_schedule)
thread.start()

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
