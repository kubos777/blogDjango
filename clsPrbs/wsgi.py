"""
WSGI config for clsPrbs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clsPrbs.settings")

application = get_wsgi_application()



'''


Archivo WSGI de configuracion en pythonanywhere:
from django.core.wsgi import get_wsgi_application
import	os
import	sys

path	=	'/home/kubos777/clsPrbs'
if	path	not	in	sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'clsPrbs.settings'

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clsPrbs.settings")

#application = get_wsgi_application()

from	whitenoise.django	import	DjangoWhiteNoise

application	=	DjangoWhiteNoise(get_wsgi_application())

'''

