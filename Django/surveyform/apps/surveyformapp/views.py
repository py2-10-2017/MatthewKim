# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,"surveyformapp/index.html")

def process(request):
    if 'count' not in request.session:
        request.session['count']=1
    else:
        request.session['count']+=1
    request.session['name']=request.POST['name']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['comment']=request.POST['comment']
    return redirect('/result')

def result(request):
    context={
        'name':request.session['name'],
        'location':request.session['location'],
        'language':request.session['language'],
        'comment':request.session['comment']
    }
    return render(request, "surveyformapp/result.html",context)

# Create your views here.
