from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView


from .forms import ItemForm
from .models import Item


class ItemListView(ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		return context

class ItemDetailView(DetailView):

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin,CreateView):
	# This form would be passed to the template below.
	form_class = ItemForm
	# This template is saved at the src template folder.
	template_name = "form.html"

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def form_valid(self,form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super().form_valid(form)

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs["user"] = self.request.user
		# kwargs["text"] = "Hello there"
		return kwargs

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = "Add Menu Item"
		return context


class ItemUpdateView(LoginRequiredMixin,UpdateView):
	form_class = ItemForm
	# template_name = "form.html"
	template_name = "menus/detail-update.html"

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Edit Menu Item"
		return context

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs["user"] = self.request.user
		return kwargs