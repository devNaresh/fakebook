"""
WSGI config for fakebook project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys, site

SITE_DIR = '/home/ubuntu/fakebook/'
site.addsitedir(SITE_DIR)
sys.path.append(SITE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'fakebook.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
