#coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from production.ping.models import Ping


@login_required(login_url='/')
def list(request):
    """
        Must be return the list of ping tests
    """
    pings = Ping.objects.all()

    return render(request, 'ping/index.html', {'pings': pings})
