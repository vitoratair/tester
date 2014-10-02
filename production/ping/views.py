#coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from production.ping.models import Ping



@login_required(login_url='/')
def list(request):
    """
        Must be return the list of ping tests
    """
    pings = Ping.objects.all()

    return render(request, 'ping/index.html', {'pings': pings})


def delete(request, ping):
	"""
	Must be deleted a ping test
	"""

	Ping.objects.filter(pk=ping).delete()

	json = serializers.serialize('json', Ping.objects.all())

	return HttpResponse(json, mimetype='application/json')