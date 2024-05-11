import os

from kombu import Exchange, Queue

# Celery
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "")

CELERY_RESULT_BACKEND = "django-db"
CELERY_TASK_DEFAULT_QUEUE = "default"

CELERY_TASK_QUEUES = (
    Queue("default", Exchange("default"), routing_key="default.#"),
    # scrapers
    Queue("scrapers", Exchange("scrapers"), routing_key="scrapers.#"),
)

CELERY_TASK_ROUTES = {
    "lib.scrapers.*": {"queue": "scrapers"},
}