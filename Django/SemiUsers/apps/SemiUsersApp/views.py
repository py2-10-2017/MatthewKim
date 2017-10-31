# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import *

# Create your views here.
def index(request):
    return render(request,"SemiUsersApp/index.html", {"users":Users.objects.all()})

def new(request):
    return render(request,'SemiUsersApp/new.html')

def edit(request, user_id):
    return render(request, 'SemiUsersApp/edit.html',{"user":Users.objects.get(id=user_id)})

def show(request,user_id):
    return render(request,'SemiUsersApp/profile.html', {"user":Users.objects.get(id=user_id)})

def create(request):
    Users.objects.create(full_name=request.POST['full_name'], email=request.POST['email'])
    return redirect('/users')

def destroy(request,user_id):
    Users.objects.get(id=user_id).delete()
    return redirect('/users')

def update(request, user_id):
    user=Users.objects.get(id=user_id)
    user.full_name=request.POST['full_name']
    user.email=request.POST['email']
    user.save()
    return redirect('/users')
