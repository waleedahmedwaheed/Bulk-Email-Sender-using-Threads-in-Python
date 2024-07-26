# Bulk Email Sender

This repository contains a Python script for sending bulk emails using SMTP credentials. The script uses the smtplib and email libraries, and sends emails concurrently using threads for faster operation.

## Requirements

- Python 3.6 or higher
- A valid SMTP server and credentials

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/waleedahmedwaheed/Bulk-Email-Sender-using-Threads-in-Python.git
    cd bulk-email-sender
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `config.json` file in the project root with your SMTP credentials and email details:

    ```plaintext
    {
		"smtp_server": "smtp.example.com",
		"smtp_port": 587,
		"smtp_username": "your-email@example.com",
		"smtp_password": "your-email-password",
		"from_email": "your-email@example.com",
		"subject": "Your Email Subject",
		"body": "This is the body of your email."
	}
    ```
	
4. Create a `recipients.txt` file in the project root with the list of email addresses (one per line):
	
	```plaintext
		recipient1@example.com
		recipient2@example.com
		recipient3@example.com
	```

## Usage

1. Run the `bulk_email_sender.py` script:
    ```bash
    python bulk_email_sender.py
    ```