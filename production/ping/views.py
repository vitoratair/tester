# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from production.ping.models import Ping, PingProduct
from django.core.urlresolvers import reverse


@login_required(login_url='/')
def list(request):
    """
        Must be return the list of ping tests
    """
    pings = Ping.objects.all()

    return render(request, 'ping/index.html', {'pings': pings})


def deleteProduct(request, ping, product):
    """
    Must be deleted a ping test
    """

    PingProduct.objects.filter(pk=ping).delete()
    pings = PingProduct.objects.filter(product=product)

    return HttpResponseRedirect('/product/showTest/' + product + '/')
