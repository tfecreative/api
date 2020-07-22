from django.core.mail import send_mail
from django.utils.html import strip_tags
from tfecreative import settings


def send_email(recipients, subject, body, from_email=None):
    send_mail(
        subject=subject,
        message=strip_tags(body),
        from_email=from_email or settings.NO_REPLY_EMAIL,
        recipient_list=recipients,
        html_message=body,
        fail_silently=False,
    )
