from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):

	context = {"hello":"saurabh"}
	return render(request,'home.html',context)


def about(request):

	context = {}
	return render(request,'about.html',context)

def contact(request):

	context = {}
	return render(request,'contact.html',context)