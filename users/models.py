import hashlib

from django.contrib.auth.models import User as BaseUser


class User(BaseUser):
    class Meta:
        proxy = True
