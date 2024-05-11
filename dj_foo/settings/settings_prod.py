import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# These settings are imported in main settings.py if ENV=PROD

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PG_DBNAME", ""),
        "USER": os.environ.get("PG_DBUSER", ""),
        "PASSWORD": os.environ.get("PG_DBPWD", ""),
        "HOST": os.environ.get("PG_HOST", ""),
        "PORT": int(os.environ.get("PG_PORT", 5432)),
    },
}

# SMTP settings
EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 25))
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", "True").lower() == "true"
DEFAULT_SENDER = os.environ.get("DEFAULT_SENDER", "foo@example.com")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

