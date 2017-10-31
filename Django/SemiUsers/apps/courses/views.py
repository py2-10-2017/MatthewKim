# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages import error
from django.shortcuts import render, redirect
from models import *

def index(request):
    return render(request,"courses/index.html", {"Courses":Courses.objects.all()})

def add(request):
    errors=Courses.objects.basic_validator(request.POST)
    if errors:
        for tag,err in errors.iteritems():
            error(request,err,extra_tags=tag)
        return redirect('/courses')
    else:
        Courses.objects.create(name=request.POST['name'],desc=request.POST['desc'])
        return redirect('/courses')

def destroy(request,course_id):
    return render(request,"courses/destroy.html", {"course":Courses.objects.get(id=course_id)})

def destroying(request, course_id):
    Courses.objects.get(id=course_id).delete()
    return redirect('/courses')
