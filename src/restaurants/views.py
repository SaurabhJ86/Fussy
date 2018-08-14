from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.

# def home(request):

# 	context = {"hello":"saurabh"}
# 	return render(request,'home.html',context)


class HomeView(TemplateView):

	template_name = "home.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context["hello"] = "Saurabh"
		return context

# Using the below two as Template Based Views in the url's file.
# def about(request):

# 	context = {}
# 	return render(request,'about.html',context)

# def contact(request):

# 	context = {}
# 	return render(request,'contact.html',context)

# Not using CBV
# class ContactView(View):

# 	def get(self,request, *args, **kwargs):

# 		context = {}
# 		return render(request, 'contact.html',context)

# Although this is Template Based View, but using it in url's is more efficient
# class ContactTemplateView(TemplateView):
# 	template_name = "contact.html"