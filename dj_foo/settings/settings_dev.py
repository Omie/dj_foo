import os       # noqa

from pathlib import Path

# These settings are imported in main settings.py if ENV=DEV

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
