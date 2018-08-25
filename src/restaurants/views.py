from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView


# Create your views here.
from .forms import RestaurantLocationCreateForm
from .models import RestaurantLocation


class RestaurantListView(LoginRequiredMixin,ListView):
	# This is being used to override the get_queryset method so that it can return dynamic queryset.
	def get_queryset(self):
		queryset = RestaurantLocation.objects.filter(owner=self.request.user)
		# slug = self.kwargs.get("slug")
		# if slug:
		# 	queryset = RestaurantLocation.objects.filter(
		# 		Q(category__iexact=slug)|
		# 		Q(category__icontains=slug)
		# 		)
		# else:
		# 	queryset = RestaurantLocation.objects.all()

		return queryset


class RestaurantDetailView(LoginRequiredMixin,DetailView):
	def get_queryset(self):
		queryset = RestaurantLocation.objects.filter(owner=self.request.user)
		return queryset

class RestaurantCreateView(LoginRequiredMixin,CreateView):
	form_class = RestaurantLocationCreateForm
	# template_name = 'restaurants/form.html'
	template_name = 'form.html'
	# login_url = '/login/'
	# Have created get_absolute_url.
	# success_url = '/restaurants/'

	def form_valid(self,form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super().form_valid(form)

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = "Add Restaurant"
		return context



class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
	form_class = RestaurantLocationCreateForm
	# template_name = 'form.html'
	template_name = "restaurants/detail-update.html"
	# I can use the below when I do not want any dynamic data. If I need to use this, then I need to remove the get_queryset
	# queryset = RestaurantLocation.objects.all()

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = "Update Restaurant"
		return context

	def get_queryset(self):
		queryset = RestaurantLocation.objects.filter(owner=self.request.user)
		return queryset