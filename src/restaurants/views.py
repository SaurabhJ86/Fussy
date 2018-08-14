from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.

from .models import RestaurantLocation

def restaurant_listView(request):

	template = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {"restaurants":queryset}
	return render(request,template,context)