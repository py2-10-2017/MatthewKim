# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
from django.utils import timezone
email_regex=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UsersManager(models.Manager):
    def validator(self,postData):
        errors={}
        if len(postData['name'])<2:
            errors['last_name']="Your name must be at least 2 characters"
        if not email_regex.match(postData['email']):
            errors['email']="Your email is not valid"
        if len(postData['pw'])<8:
            errors['pw']="Your password must be at least 8 characters"
        if postData['pw']!=postData['pw_c']:
            errors['pw_c']="Your passwords do not match"
        return errors

class Users(models.Model):
    name=models.CharField(max_length=255)
    alias=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    pw=models.CharField(max_length=255)
    objects=UsersManager()

class Books(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    review=models.TextField()
    stars=models.IntegerField()
    user=models.ForeignKey(Users,related_name="reviews")
    book=models.ForeignKey(Books,related_name="reviews")
    created_at=models.DateTimeField(auto_now_add=True)
