# Task Automation App

This app automates various tasks and sends emails using SMTP.

## Email Configuration
Before running the app, update `app.py` with your own email credentials:

```python
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  
app.config['MAIL_PASSWORD'] = 'your_email_password'    
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

     Replace `your_email@gmail.com` and `your_email_password` with your actual credentials.

     ## Requirements
     - Python 3.x
     - Flask
     - Flask-Mail

     ## Installation
     To install the required dependencies, run:
     
     ```bash
     pip install -r requirements.txt
     ```

     ## Usage
     Run the app using:

     ```bash
     python app.py
     ```

     Happy automating! 😊
     ```

