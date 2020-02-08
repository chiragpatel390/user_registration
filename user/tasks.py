from celery import shared_task
from django.contrib.auth.models import User


@shared_task
def get_users():
    print(User.objects.all())
    return
