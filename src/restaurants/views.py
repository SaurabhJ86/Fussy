from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.db.models import Q
# Create your views here.

from .models import RestaurantLocation

def restaurant_listView(request):

	template = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {"object_list":queryset}
	return render(request,template,context)


class RestaurantListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug)|
				Q(category__icontains=slug)
				)
		else:
			queryset = RestaurantLocation.objects.all()

		return queryset


# class SearchRestaurantListView(ListView):
# 	template_name = 'restaurants/restaurants_list.html'

# 	def get_queryset(self):
# 		slug = self.kwargs.get("slug")
# 		if slug:
# 			queryset = RestaurantLocation.objects.filter(
# 				Q(category__iexact=slug)|
# 				Q(category__icontains=slug)
# 				)
# 		else:
# 			queryset = RestaurantLocation.objects.none()
# 		return queryset