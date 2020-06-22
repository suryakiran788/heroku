from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myhome(request):
	return HttpResponse("hai")
def page1(request):
	return render(request,'test.html')
