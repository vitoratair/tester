# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from production.ping.models import Ping, PingProduct
from production.product.models import Product


@login_required(login_url='/')
def list(request):
    """
        Must be return the list of ping tests
    """
    pings = Ping.objects.all()

    products = Product.objects.all()
    return render(request, 'ping/index.html', {'products': products,
                                               'pings': pings})


def deleteProduct(request, ping, product):
    """
    Must be deleted a ping test of product
    """

    PingProduct.objects.filter(pk=ping).delete()
    PingProduct.objects.filter(product=product)

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

    print  result
    try:
        a = PingProduct(ping_id=ping, product_id=product, result=result)
        a.save()
    except Exception, e:
        print e


    pings = Ping.objects.all()
    json = serializers.serialize("json", pings)

    return HttpResponse(json, mimetype='application/json')
