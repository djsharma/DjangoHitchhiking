from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def basic(request):

	if request.method == 'POST':
		print(request.body)
		response = HttpResponse('recieved message')
		return response
	else:

		response = HttpResponse('Method not supported')
		response.status_code = 404
		return response