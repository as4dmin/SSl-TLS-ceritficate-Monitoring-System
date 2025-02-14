import datetime
import ssl
import socket
import os
import smtplib
import logging
import re
from email.mime.text import MIMEText

# Configure Logging
logging.basicConfig(filename="ssl_monitor.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def is_valid_domain(domain):
    """Validate the domain name."""
    domain_regex = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    return re.match(domain_regex, domain) is not None

def is_valid_email(email):
    """Validate email address."""
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None

def get_certificate(hostname, port=443):
    """Fetch SSL/TLS certificate from the domain."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
        logging.info(f"Successfully retrieved SSL certificate for {hostname}")
        return cert
    except (ssl.SSLError, socket.timeout, socket.gaierror) as e:
        logging.error(f"[ERROR] SSL Error for {hostname}: {e}")
        return None

def check_expiration(cert, hostname):
    """Check if SSL certificate is expiring soon."""
    if not cert:
        return f"[ALERT] Could not retrieve SSL certificate for {hostname}"

    expiry_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    expiry_date = expiry_date.replace(tzinfo=datetime.timezone.utc)
    now = datetime.datetime.now(datetime.timezone.utc)
    remaining_days = (expiry_date - now).days

    if remaining_days <= 30:
        return f"[WARNING] SSL certificate for {hostname} is expiring in {remaining_days} days!"
    return f"[INFO] SSL certificate for {hostname} is valid. Expires in {remaining_days} days."

def send_email_notification(subject, message, recipient_email):
    """Send an email notification when an SSL certificate is expiring."""
    sender_email = os.getenv("EMAIL_USER")		
    sender_password = os.getenv("EMAIL_PASS")

    if not sender_email or not sender_password:
        print("[ERROR] Email credentials are missing!")
        return

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            logging.info("[INFO] Email notification sent.")
    except Exception as e:
        logging.error(f"[ERROR] Failed to send email: {e}")

#Run SSL Monitoring
while True:
    domain = input("Enter domain (or 'exit' to quit): ").strip()
    if domain.lower() == "exit":
        break
    if not is_valid_domain(domain):
        print("[ERROR] Invalid domain name.")
        continue

    cert_info = get_certificate(domain)
    if cert_info:
        message = check_expiration(cert_info, domain)
        print(message)
        if "expiring" in message:
            recipient_email = input("Enter recipient email: ").strip()
            if is_valid_email(recipient_email):
                send_email_notification("SSL Expiry Alert", message, recipient_email)
            else:
                print("[ERROR] Invalid email.")
