# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CoursesManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['name'])<5:
            errors['name']="Course name should be longer than 5 characters"
        if len(postData['desc'])<15:
            errors['desc']="Course description should be longer than 15 characters"
        return errors

class Courses(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    objects=CoursesManager()
