import smtplib
import random
import string
import sqlite3
from email.mime.text import MIMEText

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Retrieve a random user email from the database
cursor.execute("SELECT email FROM users ORDER BY RANDOM() LIMIT 1")
result = cursor.fetchone()
if result is None:
    print("No user found in the database.")
    exit()
user_email = result[0]

# Generate a random verification code
verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Send the MFA email
try:
    # SMTP configuration
    smtp_server = "your_smtp_server"
    smtp_port = 587
    smtp_username = "your_smtp_username"
    smtp_password = "your_smtp_password"

    # Email details
    sender_email = "your_sender_email"
    subject = "Multi-Factor Authentication Code"
    message = f"Your verification code is: {verification_code}"

    # Create the email
    msg = MIMEText(message)
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Subject'] = subject

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

    print("MFA email sent successfully!")
except smtplib.SMTPException as e:
    print("Error sending MFA email:", e)

# Close the database connection
conn.close()
