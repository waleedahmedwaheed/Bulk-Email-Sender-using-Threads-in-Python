import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Thread
import logging

# Load SMTP configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

smtp_server = config['smtp_server']
smtp_port = config['smtp_port']
smtp_username = config['smtp_username']
smtp_password = config['smtp_password']
from_email = config['from_email']
subject = config['subject']
body = config['body']

# Load recipients
with open('recipients.txt', 'r') as recipients_file:
    recipients = [line.strip() for line in recipients_file]

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to send an email
def send_email(recipient):
    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, recipient, msg.as_string())
        server.quit()
        
        logging.info(f'Successfully sent email to {recipient}')
    except Exception as e:
        logging.error(f'Failed to send email to {recipient}: {e}')

# Create and start threads
threads = []
for recipient in recipients:
    thread = Thread(target=send_email, args=(recipient,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
