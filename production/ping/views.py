# coding: utf-8
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from production.ping.forms import PingForm
from production.ping.models import Ping, PingProduct
from production.product.models import Product
from production.ping.library.execPing import ExecPing
from production.core.headers import *


@login_required(login_url='/')
def list(request):
    """
        Must be return the list of ping tests
    """

    pings = Ping.objects.all()

    products = Product.objects.filter(test=PING).all()

    return render(request, 'ping/index.html', {'products': products,
                                               'pings': pings})


def add(request):
    """
        Must be return the template to save a new ping
    """

    if request.method == 'GET':
        return render(request, 'ping/add.html', {'form': PingForm()})

    form = PingForm(request.POST)

    if not form.is_valid():
        return render(request, 'ping/add.html', {'form': form})

    form.save()
    return HttpResponseRedirect('/ping/')


def deleteProduct(request, ping, product):
    """
    Must be deleted a ping test of product
    """

    PingProduct.objects.filter(pk=ping).delete()

    return HttpResponseRedirect('/product/showTest/' + product + '/')


def delete(request, ping):
    """
    Must be deleted a ping test of system
    """

    Ping.objects.filter(pk=ping).delete()
    pings = Ping.objects.all()
    json = serializers.serialize("json", pings)

    return HttpResponse(json, mimetype='application/json')


def addProduct(request, ping, product, result):
    """
    Must be saved a ping test into a product
    """

    try:
        a = PingProduct(ping_id=ping, product_id=product, result=result)
        a.save()
    except Exception, e:
        print e

    pings = Ping.objects.all()
    json = serializers.serialize("json", pings)

    return HttpResponse(json, mimetype='application/json')


def initializeTests(request):
    """
    Must be initialized all ping tests of a product
    """

    defaultProduct = Product.objects.filter(default=DEFAULT).get()
    tests = PingProduct.objects.filter(product=defaultProduct.id).all()

    if defaultProduct.accessMethod == SSH:
        testsPing = ExecPing(tests, defaultProduct.id, SSH_USER, SSH_PASSWORD)

    return HttpResponse(json.dumps({'data': 'Finish'}), mimetype="application/json")
