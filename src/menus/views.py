from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView


from .forms import ItemForm
from .models import Item


class ItemListView(ListView):

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)


class ItemCreateView(CreateView):
	form_class = ItemForm
	template_name = "form.html"

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def form_valid(self,form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super().form_valid(form)

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = "Add Menu Item"
		return context


class ItemUpdateView(UpdateView):
	form_class = ItemForm

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Add Menu Item"
		return context