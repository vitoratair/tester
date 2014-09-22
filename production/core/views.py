#coding: utf-8

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
import commands
import json
import time
from production.core.production_commands import *

def home(request):
	"""
		Must be return the index template
	"""

	return render(request, 'index_first.html')

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