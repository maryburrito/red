#!/bin/bash

/usr/bin/env python manage.py migrate

/usr/bin/env python manage.py collectstatic --noinput --clear

/usr/bin/env gunicorn red.wsgi:application -w 2 -b :${GUNICORN_PORT-8000}

