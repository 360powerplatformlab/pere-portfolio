from flask import Flask, request, render_template, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for flash messages

# ==========================
# CONFIGURATION
# ==========================
EMAIL_ADDRESS = "wperestar@yahoo.com"       # Sender email (also your inbox)
EMAIL_PASSWORD = "xctysilpsygwjlhj"          # Use app password for Gmail/Outlook
SMTP_SERVER = "imap.mail.yahoo.com"                # Change if using Outlook or others
SMTP_PORT = 465

# ==========================
# ROUTES
# ==========================

@app.route('/')
def index():
    return render_template('contact.html')  # Make sure contact.html is in "templates/" folder

@app.route('/send', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Validate inputs
    if not name or not email or not message:
        flash("All fields are required.")
        return redirect(url_for('index'))

    # Compose email
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg = MIMEText(body)
    msg['Subject'] = 'Portfolio Contact Form Submission'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS  # Email goes to your inbox

    try:
        # Connect to SMTP server and send email
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        flash("Message sent successfully!")
        return redirect(url_for('index'))

    except Exception as e:
        print("Error sending email:", e)
        flash("Failed to send message. Please try again later.")
        return redirect(url_for('index'))

# ==========================
# RUN SERVER
# ==========================
if __name__ == '__main__':
    app.run(debug=True)
