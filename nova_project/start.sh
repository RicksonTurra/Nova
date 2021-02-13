#!/bin/bash

if [ -f "db.sqlite3" ]; then
    python manage.py runserver 0.0.0.0:8000
else 
    python manage.py migrate && python manage.py runserver 0.0.0.0:8000
fi