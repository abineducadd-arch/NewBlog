"""
WSGI config for Electronics project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
settings_module = 'Electronics.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'Electronics.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
