import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Config.settings')
application = get_wsgi_application()
print("WSGI application is loaded:", application)