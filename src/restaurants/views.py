from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import ListView,DetailView,TemplateView

from django.db.models import Q
# Create your views here.

from .models import RestaurantLocation

def restaurant_listView(request):

	template = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {"object_list":queryset}
	return render(request,template,context)


class RestaurantListView(ListView):
	def get_context_data(self,**kwargs):
		# print(self.kwargs,kwargs)
		context = super().get_context_data(**kwargs)
		print(context)
		return context

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


class RestaurantDetailView(DetailView):
	# This is only showing purpose.
	# template_name = 'restaurants/restaurantLocation_DetailView.html'
	queryset = RestaurantLocation.objects.all()

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		return context

	def get_object(self,**kwargs):
		rest_id = self.kwargs.get("rest_id")
		obj = get_object_or_404(RestaurantLocation,pk=rest_id)
		return obj














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