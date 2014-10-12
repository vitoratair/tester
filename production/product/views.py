from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from production.product.models import Product
from production.product.forms import ProductForm
from production.ping.models import Ping
from production.ping.models import PingProduct as PingProduct
from django.core import serializers
from production.product.testCommands import *


def list(request):
    """
        Must be return a list of products or save a new product on database
    """

    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if not form.is_valid():
            return render(request, 'products/index.html', {'products': products,
                                                           'form': form})
        form.save()

    return render(request, 'products/index.html', {'form': ProductForm(),
                                                   'products': products})


def getTest(request, product):
    """

    """

    # ids = Product.objects.values_list('id', flat=True).filter(pk=product)

    # pings = Ping.objects.filter(ap_id__in=set(ids))

    pings = Product.objects.all()

    json = serializers.serialize(
        "json", [pings], indent=4, relations=('object_type', 'individual',))

    return HttpResponse(json, mimetype='application/json')


def delete(request, product):

    Product.objects.filter(pk=product).delete()
    return HttpResponseRedirect('/product/list/')


def showTest(request, product):
    """
        Must be returned a list of tests associated with product
    """

    productName = Product.objects.filter(pk=product).get()

    tests = Product.objects.values_list('test', flat=True).filter(pk=product[0])

    pings = PingProduct.objects.filter(product=product)

    return render(request, 'products/product_tests.html', {'pings': pings,
                                                           'product': productName})
