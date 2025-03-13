from celery import Celery

consumer1 = Celery(
    'consumer1',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
)

consumer1.conf.update(
    broker_connection_retry_on_startup=True
)

# Importing tasks here is necessary to avoid circular imports
import tasks