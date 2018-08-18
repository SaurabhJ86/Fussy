from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import ListView,DetailView,TemplateView,CreateView

from django.db.models import Q
# Create your views here.
from .forms import RestaurantLocationCreateForm
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

class RestaurantCreateView(CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurants/form.html'
	success_url = '/restaurants/'
