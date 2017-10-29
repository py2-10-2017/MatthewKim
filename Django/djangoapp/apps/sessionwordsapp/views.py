# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def session_word(request):
    return render(request,"sessionwordsapp/session_word.html")

def add(request):
    try:
        request.session['words']
    except:
        request.session['words']=[]

    word={}
    for key,value in request.POST.iteritems():
        if key!="csrfmiddlewaretoken" and key!="big":
            word[key]=value
        if key=="big":
            if key=="big":
                word[key]="20px"
            else:
                word[key]=""
    word['time']="- added on "+strftime("%H:%M, %B %d, %Y",gmtime())
    temp=request.session['words']
    temp.append(word)
    request.session['words']=temp
    print request.session['words']
    #request.session['big'].append(False)
    return redirect('/session_word')

def clear(request):
    del request.session['words']
    return redirect('/session_word')

# Create your views here.
