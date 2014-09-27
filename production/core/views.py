#coding: utf-8

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import commands
import json
import time
from production.core.production_commands import *
from production.product.models import Product


@login_required(login_url='/')
def home(request):
	"""
		Must be return the index template or test template if already has a default product on the system
	"""

	if Product.objects.filter(default=1).count() == 0:
		products = Product.objects.all()
		return render(request, 'index_first.html', {'products':products})

	return render(request, 'test.html')


def setDefaultProduct(request):
	"""
		Must be set a new product as default
	"""

	product = request.POST['product']
	Product.objects.all().update(default=0)
	Product.objects.filter(pk=product).update(default=1)

	return HttpResponseRedirect('/core/')


def testBoard(request):
	"""
		Must be return the test template
	"""

	return render(request, 'test.html')


def testStatus(request):
	"""
		Must be return the json message about interface status
	"""

	data = {}

	if getStatus():
		data['message'] = BOARD_FOUND
	else:
		data['message'] = BOARD_NOT_FOUND

	return HttpResponse(json.dumps(data), mimetype = "application/json")


def getStatus():
	"""
		Must be return the status on ethernet device
	"""

	status = commands.getoutput("ifconfig en3")

	if status.find(ACTIVE_VALUE) == NOT_FIND:
		return False

	return True