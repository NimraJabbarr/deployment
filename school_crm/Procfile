release: python manage.py migrate
release: python manage.py collectstatic --noinput
web: gunicorn school_crm.wsgi:application --bind 0.0.0.0:8080
