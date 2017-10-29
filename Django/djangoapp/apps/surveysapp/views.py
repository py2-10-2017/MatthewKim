# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    response="placeholder to display all the surveys created"
    return HttpResponse(response)

def new(response):
    response="placeholder for users to add a new survey"
    return HttpResponse(response)
# Create your views here.
