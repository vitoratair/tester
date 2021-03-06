# coding: utf-8

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import commands
import json
from production.core.headers import *
from production.product.models import Product
from production.core.models import Information


@login_required(login_url='/')
def home(request):
    """
            Must be return the index template or test template if already has a
            default product on the system
    """

    if Product.objects.filter(default=1).count() == 0:
        products = Product.objects.all()
        return render(request, 'index_first.html', {'products': products})

    defaultProduct = Product.objects.filter(default=1).get()

    return render(request, 'test.html', {'product': defaultProduct})


def setDefaultProduct(request):
    """
            Must be set a new product as default
    """

    product = request.POST['product']
    Product.objects.all().update(default=0)
    Product.objects.filter(pk=product).update(default=1)

    return HttpResponseRedirect('/core/')


def testStatus(request):
    """
            Must be return the json message about interface status
    """

    data = {}

    if getStatus():
        data['message'] = BOARD_FOUND
    else:
        data['message'] = BOARD_NOT_FOUND

    return HttpResponse(json.dumps(data), mimetype="application/json")


def getStatus():
    """
        Must be return the status on ethernet device
    """

    interface = Information.objects.filter(pk=1).get().interface

    status = commands.getoutput("ifconfig " + interface)

    if status.find(ACTIVE_VALUE) == NOT_FIND:
        return False

    return True
