
"""
Notification utilities for sending alerts.
"""

from flask_mail import Message
from .. import mail

def send_email(subject, recipients, body):
    msg = Message(subject, recipients=recipients, body=body)
    mail.send(msg)
