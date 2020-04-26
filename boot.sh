#!/bin/sh
exec gunicorn -b :5000 --timeout 400 --workers 2 --access-logfile - --error-logfile - main:main_app
