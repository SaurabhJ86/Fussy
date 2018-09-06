from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,View


from menus.models import Item
from restaurants.models import RestaurantLocation

from .models import Profile

User = get_user_model()

class ProfileFollowToggle(LoginRequiredMixin,View):
	def post(self,request,*args,**kwargs):
		user_to_toggle = request.POST.get("username").strip()
		profile,is_following = Profile.objects.toggle_follow(request.user,user_to_toggle)

		# The below is the profile which we need to follow/remove
		# profile = Profile.objects.get(user__username__iexact=user_to_toggle)
		# # The below will check whether the logged in user is in the followers list of the above profile.
		# if request.user in profile.followers.all():
		# 	profile.followers.remove(request.user)
		# else:
		# 	profile.followers.add(request.user)
		return redirect(f"/profile/{profile}/")

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
		# The below three lines are important as they would dictate whether we want a Follow button or UnFollow button.
		is_following = False
		if user.profile in self.request.user.is_following.all():
			is_following = True
		context["is_following"] = is_following
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
