# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, "amadon/index.html")

def buy(request):
    try:
        request.session['price']
    except:
        request.session['price']=0
        request.session['quantity']=0
    for key, value in request.POST.iteritems():
        if key=="product_id":
            if value=="1":
                price=19.99
            elif value=="2":
                price=29.99
            elif value=="3":
                price=19.99
            elif value=="4":
                price=49.99
        if key=="quantity":
            quantity=int(value)
            total_cost=price*quantity
            print total_cost
    request.session['cost']=total_cost
    request.session['quantity']+=quantity
    request.session['price']+=total_cost
    return redirect("/amadon/checkout")

def checkout(request):
    return render(request,"amadon/checkout.html")

def clear(request):
    del request.session['quantity']
    del request.session['cost']
    del request.session['price']
    return redirect("/amadon")

# Create your views here.
