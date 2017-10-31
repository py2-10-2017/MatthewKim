# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib.messages import error
from django.shortcuts import render,redirect
import bcrypt

def index(request):
    return render(request,"LoginAndReg/index.html")

def success(request):
    return render(request,"LoginAndReg/success.html", {"user":Users.objects.get(id=request.session['id'])})

def login(request):
    try:
        user=Users.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['pw'].encode(),user.pw.encode())==True:
            request.session['id']=user.id
            return render(request,"LoginAndReg/success.html", {"user":Users.objects.get(id=request.session['id'])})
        else:
            errors={}
            errors['LoginFail']="Password is incorrect"
            for tag,err in errors.iteritems():
                error(request,err,extra_tags=tag)
            return redirect('/')
    except:
        errors={}
        errors['LoginFail']="Your email and password do not match"
        for tag,err in errors.iteritems():
            error(request,err,extra_tags=tag)
        return redirect('/')

def register(request):
    errors=Users.objects.validator(request.POST)
    if errors:
        for tag,err in errors.iteritems():
            error(request,err,extra_tags=tag)
        return redirect('/')
    else:
        pw_hash=bcrypt.hashpw(request.POST['pw'].encode(),bcrypt.gensalt())
        Users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],pw=pw_hash)
        request.session['id']=Users.objects.get(email=request.POST['email']).id
        return redirect('/success')
# Create your views here.
