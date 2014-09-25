# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from production.login.forms import LoginForm
from production.login.models import Login
import json


def home(request):
    """
        Esse método tem por objetivo exibir o template para logim do usuário
    """

    loginNumbers = Login.objects.count()

    if loginNumbers == 0:
        db = Login(email='admin@admin.com.br', password='admin', username='admin', perfil_id=1)
        db.save()

    return render(request, 'login/index.html')


def validate(request):
    """
        Esse método tem por objetivo verificar
        no banco de dados as credenciais de username e password do usuário
    """

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

    if Login.objects.filter(password=password, username=username).count() == 0:
        return render(request, 'login/index.html')

    return HttpResponseRedirect('/core/')

