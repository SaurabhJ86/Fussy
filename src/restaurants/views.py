from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import ListView,DetailView,TemplateView,CreateView


# Create your views here.
from .forms import RestaurantLocationCreateForm
from .models import RestaurantLocation

@login_required(login_url="/login/")
def restaurant_createView(request):
	form = RestaurantLocationCreateForm(request.POST or None)
	if form.is_valid():
		if request.user.is_authenticated():
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			return HttpResponseRedirect("/restaurants/")
		else:
			return HttpResponseRedirect("/login/")

	template = "restaurants/form.html"
	context = {"form":form}
	return render(request,template,context)

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

class RestaurantCreateView(LoginRequiredMixin,CreateView):
	form_class = RestaurantLocationCreateForm
	template_name = 'restaurants/form.html'
	# login_url = '/login/'
	success_url = '/restaurants/'

	def form_valid(self,form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super().form_valid(form)








