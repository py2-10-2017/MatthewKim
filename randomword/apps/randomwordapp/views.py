# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    unique_id = get_random_string(length=6)
    if not 'attempt' in request.session:
        request.session['attempt']=1
    else:
        request.session['attempt']+=1
    context={
        'random':unique_id,
        'attempt':request.session['attempt']
    }
    return render(request,"randomwordapp/index.html",context)

def reset(request):
    del request.session['attempt']
    return redirect('/')
