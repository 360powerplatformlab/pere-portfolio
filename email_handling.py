from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('contact.html').read())

@app.route('/send', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Prepare email content
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg = MIMEText(body)
    msg['Subject'] = 'Portfolio Contact Form Submission'
    msg['From'] = 'youremail@example.com'  # Must be a valid sender
    msg['To'] = 'youremail@example.com'    # Your inbox

    # Send email via SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login('youremail@example.com', 'YOUR_EMAIL_PASSWORD')  # App password if using Gmail
        server.send_message(msg)

    return "Message sent successfully!"
    
if __name__ == "__main__":
    app.run(debug=True)
