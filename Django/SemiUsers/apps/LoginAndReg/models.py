# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
email_regex=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UsersManager(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['first_name']="Your first name must be at least 2 characters"
        if len(postData['last_name'])<2:
            errors['last_name']="Your last name must be at least 2 characters"
        if not email_regex.match(postData['email']):
            errors['email']="Your email is not valid"
        if len(postData['pw'])<8:
            errors['pw']="Your password must be at least 8 characters"
        if postData['pw']!=postData['pw_c']:
            errors['pw_c']="Your passwords do not match"
        return errors

class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    pw=models.CharField(max_length=255)
    pw_c=models.CharField(max_length=255)
    objects=UsersManager()
