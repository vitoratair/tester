from django.shortcuts import render
from production.product.models import Product


def list(request):
	"""
		Must be return a list of products
	"""

	products = Product.objects.all()
	return render(request, 'products/index.html', {'products': products})
