import os

from kombu import Exchange, Queue

# Celery
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "")
CELERY_TIMEZONE = "Asia/Kolkata"
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = 'django-cache'

CELERY_TASK_DEFAULT_QUEUE = "default"

CELERY_IMPORTS = ['books.scraper']

CELERY_TASK_QUEUES = (
    Queue("default", Exchange("default"), routing_key="default.#"),
    # scrapers
    Queue("scrapers", Exchange("scrapers"), routing_key="scrapers.#"),
)

CELERY_TASK_ROUTES = {
    "books.scraper.*": {"queue": "scrapers"},
}
