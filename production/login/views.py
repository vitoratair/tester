# coding: utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from production.product.models import Product

def validate(request):
    """
        Must be validate and save the user on django session
    """
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/core/')
    else:
        return render(request, 'login/index.html')


def home(request):
    """
        Must be check if user is active or not and display the correct template.
    """

    if request.user.is_active == True:
        return HttpResponseRedirect('/core/')

    products = Product.objects.all()

    return render(request, 'login/index.html', {'products': products})

def logout(request):
    """
        Must be logout the user
    """

    Product.objects.all().update(default=0)
    auth.logout(request)

    return HttpResponseRedirect('/')