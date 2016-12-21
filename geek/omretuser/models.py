#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50,unique = True)
    password = models.CharField(max_length=200)
    email = models.EmailField(blank=False,unique = True)

    def __str__(self):
        return self.name

class UserCode(models.Model):
    user = models.OneToOneField(User,unique = True)
    user_code = models.CharField(max_length=200)
