# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse

def index(response):
    response="placeholder for users to create a new user record"
    return HttpResponse(response)

def login(reponse):
    response="placeholder for users to login"
    return HttpResponse(response)

def users(response):
    response="placeholder to later display all the list of users"
    return HttpResponse(response)
# Create your views here.
