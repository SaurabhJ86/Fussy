from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from profiles.models import Profile
from .models import Profil

"""
Note: This app was created only to revise the profile app part.
The below code will add/remove the loggeduser who is the requesting user to/from the user_to_toggle i.e. the one to be followed.
"""
class UserFollowToggle(LoginRequiredMixin,View):
	def post(self,request,*args,**kwargs):
		user_to_toggle = request.POST.get("username")
		loggedUser = request.user
		getProfile = Profile.objects.get(user__username__iexact=user_to_toggle)
		return HttpResponse("Hello there")
