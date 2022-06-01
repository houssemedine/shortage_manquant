"""
WSGI config for ShortageManagementcopie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys


from django.core.wsgi import get_wsgi_application


sys.path.append('C:/shortage_env/shortage_manquant/ShortageManagement')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ShortageManagement.settings')

application = get_wsgi_application()
