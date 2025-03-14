from celery import Celery

consumer2 = Celery(
    'consumer2',
    broker='redis://redis-svc:6379/0',
    backend='redis://redis-svc:6379/0',
)

consumer2.conf.update(
    broker_connection_retry_on_startup=True
)

# Importing tasks here is necessary to avoid circular imports
import tasks