""" Posts' utils """

from django.core.mail import send_mail
from django.conf import settings


def send_email(to_email, subject, content):
    """
        Sends email
    """
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, content, email_from, to_email)