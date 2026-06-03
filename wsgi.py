import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the school_crm directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_crm.settings')

application = get_wsgi_application()
