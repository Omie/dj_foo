#!/usr/bin/env bash

python3 manage.py collectstatic -v 0 --no-input --skip-checks

gunicorn --workers=3 dj_foo.wsgi -k gevent -b 0.0.0.0:8000
