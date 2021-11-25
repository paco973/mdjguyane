"""
WSGI config for mdj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

from mdj import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mdj.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)
application.add_files(settings.STATIC_ROOT)


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mdj.settings')

#application = get_wsgi_application()
