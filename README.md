## django-error-fix-YT

```
windows Virtula environment setup

# pip install virtualenv
# virtualenv venv
# .\venv\Scripts\activate
# pip install -r requirements.txt
# python manage.py runserver

Virtula environment deactivate command
# deactivate
```

## Redis Download here

redis downliad for windows [redis](https://github.com/tporadowski/redis/releases/)

```py

main project  ./celery.py

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project-name.settings')

app = Celery('project-name')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

```

```py
settings.py

# Celery Configuration Options
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

```

```py
task.py

from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings

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

```

```
celery event command runn
# celery -A errorfix worker -l info -P eventlet
```
