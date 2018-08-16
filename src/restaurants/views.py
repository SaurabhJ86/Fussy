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
	# This is being used to override the get_queryset method so that it can return dynamic queryset.
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
	queryset = RestaurantLocation.objects.all()

	# This is used to check whether the id is present and if it is then return it.
	def get_object(self,**kwargs):
		rest_id = self.kwargs.get("rest_id")
		obj = get_object_or_404(RestaurantLocation,pk=rest_id)
		return obj
