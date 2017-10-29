# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from random import *

def index(request):
    try:
        request.session['gold']
        request.session['activity']
        request.session['history']
    except:
        request.session['gold']=0
        request.session['activity']=[]
        request.session['history']=[]
    return render(request,"ninjagold/index.html")

def process(request):
    action={}
    if request.POST['place']=="farm":
        gold=randint(10,20)
        action['gold']=gold
    elif request.POST['place']=="cave":
        gold=randint(5,10)
        action['gold']=gold
    elif request.POST['place']=="house":
        gold=randint(2,5)
        action['gold']=gold
    elif request.POST['place']=="casino":
        gold=randint(-50,50)
        action['gold']=gold
    action['place']=request.POST['place']
    action['time']=strftime("%Y/%m/%d %I:%M %p")
    if gold>0:
        action['color']="green"
        action['activity']="Earned"
    elif gold<0:
        action['color']="red"
        action['activity']="Lost"
    else:
        action['activity']="Earned"
    temp=request.session['history']
    print action
    temp.append(action)
    request.session['history']=temp
    request.session['gold']+=gold
    return redirect('/ninjagold')

def clear(request):
    del request.session['history']
    del request.session['gold']
    return redirect('/ninjagold')
# Create your views here.
