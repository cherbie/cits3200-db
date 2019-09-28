"""
WSGI config for funding_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
# AWS deployment test
import sys
path = '/home/ubuntu/django/cits3200-db/funding-db'
if path not in sys.path:
    sys.path.append(path)
    
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'funding_project.settings')

application = get_wsgi_application()
