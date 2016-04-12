from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class CandidateUser(AbstractBaseUser):
    username = models.CharField('usuario',max_length=30,unique=True, db_index=True)
    email = models.EmailField('email', unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    def __unicode__(self):
        return self.username