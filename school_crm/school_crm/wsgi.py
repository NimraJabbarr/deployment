"""
WSGI config for school_crm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_crm.settings')

django.setup()

from django.core.wsgi import get_wsgi_application

# Run migrations on startup (only once per environment)
if not os.environ.get('MIGRATIONS_RUN'):
    try:
        call_command('migrate', verbosity=0)
        os.environ['MIGRATIONS_RUN'] = 'true'
    except Exception as e:
        print(f"Migration warning (non-fatal): {e}")

application = get_wsgi_application()
