from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
# Create your views here.

# User = settings.AUTH_USER_MODEL
User = get_user_model()

class ProfileDetailView(DetailView):
	template_name = "profiles/detail.html"
	def get_object(self):
		username = self.kwargs.get("username")
		obj = get_object_or_404(User,username__iexact=username,is_active=True)
		return obj
		# queryset = User.objects.filter(is_active=True)

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		return context
