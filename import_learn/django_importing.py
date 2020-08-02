import os, sys
sys.path.insert(0, os.path.join(os.path.abspath('..')))
import settings
from django.core.management import setup_environ
setup_environ(settings)

from django.contrib.auth.models import User
user = User.objects.filter(username='xiaofei')
print(user)
