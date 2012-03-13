import os
import sys
 
path = '/home/sa-user/workspace/mtc'
if path not in sys.path:
    sys.path.insert(0, '/home/sa-user/workspace/mtc')
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'mtc.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()