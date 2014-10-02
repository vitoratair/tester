from django.shortcuts import render, HttpResponse
from production.product.models import Product
from production.ping.models import Ping
from django.core import serializers

def list(request):
	"""
		Must be return a list of products
	"""

	products = Product.objects.all()
	return render(request, 'products/index.html', {'products': products})


def getTest(request, product):

	# ids = Product.objects.values_list('id', flat=True).filter(pk=product)

	# pings = Ping.objects.filter(ap_id__in=set(ids))

	pings = Product.objects.all()


	json = serializers.serialize( "json", [ pings ], indent = 4, relations = ('object_type', 'individual',))

	return HttpResponse(json, mimetype='application/json')
