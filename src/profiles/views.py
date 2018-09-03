from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
# Create your views here.

from menus.models import Item
from restaurants.models import RestaurantLocation
# User = settings.AUTH_USER_MODEL
User = get_user_model()

class ProfileDetailView(DetailView):
	template_name = "profiles/detail.html"
	def get_object(self):
		# print(self.request.GET)
		username = self.kwargs.get("username")
		obj = get_object_or_404(User,username__iexact=username,is_active=True)
		return obj
		# queryset = User.objects.filter(is_active=True)


	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		# Since this is a DetailView it will return the object in the context which in this case would be the name in the url.
		user = context['object']
		query = self.request.GET.get("q")
		# The search will use the QuerySet from the filter part and put another filter using query. If no query, then it would return self.
		qs = RestaurantLocation.objects.filter(owner=user).search(query)
		item_exists = Item.objects.filter(user=user).exists()
		# This to make sure that the user has created the restaurant as well as the items.
		# if query:
			# This will take the QuerySet qs created above and then this filtered by the search QuerySet.
			# qs = qs.search(query)
			# qs = RestaurantLocation.objects.search(query)
			# qs = RestaurantLocation.objects.search(user,query)
			# qs = RestaurantLocation.objects.filter(name__icontains=query)
		if qs.exists() and item_exists:
			context["locations"] = qs
		return context
