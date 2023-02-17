#!/bin/bash

#python manage.py collectstatic --noinput
uwsgi --socket :8000 --master --enable-threads --protocol=http  --module web.wsgi