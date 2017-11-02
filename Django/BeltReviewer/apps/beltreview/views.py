# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render,redirect
from django.contrib.messages import error
import bcrypt

def index(request):
    return render(request,'beltreview/index.html')

def register(request):
    errors=Users.objects.validator(request.POST)
    if errors:
        for tag,err in errors.iteritems():
            error(request,err,extra_tags=tag)
        return redirect('/')
    else:
        hash_pw=bcrypt.hashpw(request.POST['pw'].encode(),bcrypt.gensalt())
        Users.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'],pw=hash_pw)
        request.session['name']=Users.objects.get(email=request.POST['email']).name
        request.session['name']=user.name
        request.session['alias']=user.alias
        request.session['id']=user.id
        return redirect('/books')

def login(request):
    errors={}
    try:
        user=Users.objects.get(email=request.POST['email'])
        if bcrypt.checkpw(request.POST['pw'].encode(),user.pw.encode())==True:
            request.session['name']=user.name
            request.session['alias']=user.alias
            request.session['id']=user.id
            return redirect('/books')
        else:
            errors['loginfail']="Your password does not match the email"
            for tag,err in errors.iteritems():
                error(request,err,extra_tags=tag)
            return redirect('/')
    except:
        errors['loginfail']="Your email does not exist in the database"
        for tag,err in errors.iteritems():
            error(request,err,extra_tags=tag)
        return redirect('/')

def logout(request):
    del request.session['name']
    del request.session['alias']
    del request.session['id']
    return redirect('/')

def books(request):
    context={
        "books":Books.objects.all().order_by("title"),
        "recents":Reviews.objects.all().order_by("-created_at")[:3],
    }
    return render(request,'beltreview/home.html',context)

def add(request):
    return render(request,'beltreview/add.html', {"books":Books.objects.all()})

def addprocess(request):
    Books.objects.create(title=request.POST['title'],author=request.POST['author'])
    book=Books.objects.get(title=request.POST['title'])
    Reviews.objects.create(book_id=book.id,user_id=request.session['id'],review=request.POST['review'],stars=request.POST['rating'])
    return redirect('/books')

def addreview(request,book_num):
    Reviews.objects.create(user_id=request.session['id'],review=request.POST['review'], stars=request.POST['rating'],book_id=book_num)
    return redirect('/books/{}'.format(book_num))

def book(request,book_num):
    context={
        "reviews":Reviews.objects.filter(book_id=book_num),
        "book":Books.objects.get(id=book_num),
        "stars":[]
    }
    for review in context['reviews']:
        context['stars'].append(review.stars)
    return render(request,'beltreview/book.html', context)

def user(request,user_num):
    total_reviews=Reviews.objects.filter(user_id=user_num).count()
    context={
        "user":Users.objects.get(id=user_num),
        "reviews":Reviews.objects.filter(user_id=user_num),
        "total_reviews":total_reviews
    }
    return render(request,'beltreview/users.html',context)
