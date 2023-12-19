import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillaNEWS.settings')

app = Celery('skillaNews')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-weekly-newsletter': {
        'task': 'skillaNEWS.tasks.send_notifications',
        'schedule': crontab(day_of_week = 'mon', hour = '8'),
        'options': {'queue': 'weekly-news'},
    },
}