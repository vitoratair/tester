from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from production.product.models import Product
from production.product.forms import ProductForm
from production.ping.models import PingProduct as PingProduct
from django.core import serializers
from production.core.headers import *


def list(request):
    """
        Must be return a list of products or save a new product on database
    """

    paginator = Paginator(Product.objects.all(), PAGE_LIMIT)

    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if not form.is_valid():
            return render(request, 'products/index.html', {'products': products,
                                                           'form': form})
        form.save()
        return HttpResponseRedirect('/product/list/')

    return render(request, 'products/index.html', {'form': ProductForm(),
                                                   'products': products})


def getTest(request, product):
    """

    """

    pings = Product.objects.all()

    json = serializers.serialize(
        "json", [pings], indent=4, relations=('object_type', 'individual',))

    return HttpResponse(json, mimetype='application/json')


def delete(request, product):
    """
        Must be delete a product
    """

    Product.objects.filter(pk=product).delete()
    return HttpResponseRedirect('/product/list/')


def edit(request, product):
    """
        Must be edit a product using django forms
    """

    if request.method == 'GET':
        form = ProductForm(instance=Product.objects.get(pk=product))
        return render(request, 'products/edit.html', {'form': form})

    instance = Product.objects.get(pk=product)
    form = ProductForm(request.POST or None, instance=instance)

    if not form.is_valid():
        return render(request, 'products/edit.html', {'form': form})

    hasPingBefore = Product.objects.filter(test=PING)
    form.save()
    hasPingAfter = Product.objects.filter(test=PING)

    if hasPingBefore != 0 and hasPingAfter == 0:
        PingProduct.objects.filter(product=product).delete()

    return HttpResponseRedirect('/product/list/')


def showTest(request, product):
    """
        Must be returned a list of tests associated with product
    """

    pings = None

    productName = Product.objects.filter(pk=product).get()

    tests = Product.objects.values_list('test', flat=True).filter(pk=product[0])

    if PING in tests:

        paginator = Paginator(PingProduct.objects.filter(product=product), PAGE_LIMIT)

        page = request.GET.get('page')

        try:
            pings = paginator.page(page)
        except PageNotAnInteger:
            pings = paginator.page(1)
        except EmptyPage:
            pings = paginator.page(paginator.num_pages)

        print pings
    return render(request, 'products/product_tests.html', {'pings': pings,
                                                           'product': productName})
