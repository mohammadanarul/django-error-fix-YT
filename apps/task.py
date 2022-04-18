from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def sleepy(duration):
    sleep(duration)
    print("I'm busy for background working...")
    return None


@shared_task
def email_send_our_user():
    send_mail(
        'Testing celery working...',
        'celery is very awesome asyc task...',
        settings.EMAIL_HOST_USER,
        ['mdanarul7075@gmail.com'],
        fail_silently=False,
    )
    print("I'm busy for mail sending...")
    return None
