from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save

from .utils import random_string_generator

User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
	def toggle_follow(self,request_user,user_to_toggle):
		profile = Profile.objects.get(user__username__iexact=user_to_toggle)
		user = request_user
		is_following = False
		if user in profile.followers.all():
			profile.followers.remove(user)
		else:
			profile.followers.add(user)
			is_following = True
		return profile,is_following

class Profile(models.Model):
	user 			= models.OneToOneField(User)#user.profile
	followers 		= models.ManyToManyField(User,related_name="is_following",blank=True)#user.followers
	activation_key 	= models.CharField(max_length=120,blank=True,null=True)
	activated 		= models.BooleanField(default=False)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)

	objects = ProfileManager()

	def __str__(self):
		return self.user.username

	def send_activation_email(self):
		if not self.activated:
			self.activation_key = random_string_generator()
			self.save()
			path_ 				= reverse("activate",kwargs={"code":self.activation_key})
			subject 			= "Account Activation"
			from_email 			= settings.EMAIL_HOST_USER
			message 			= f"Hello{self.user.username},\n\n Please click on the below link to activate your account.\n  http:127.0.0.1:8000{path_}"
			to_email 			= [self.user.email]
			mail_confirmation 	= send_mail(subject,message,from_email,to_email,fail_silently=False)
			return mail_confirmation


def post_save_user_receiver(sender,instance,created,*args,**kwargs):
	if created:
		profile,is_created = Profile.objects.get_or_create(user=instance)
		# The below will add the created user to the followers list of user "saurabhjhingan". This is so there is some
		# data for the newly created user, otherwise it will show blank to the new user.
		default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
		default_user_profile.followers.add(instance)

		# This will add the user "saurabhjhingan" to the followers list of the new created user as well.
		# profile.followers.add(default_user_profile)
		profile.followers.add(default_user_profile.user)
		# This will add the user with id of 2 i.e. "jhingan"
		profile.followers.add(2)


post_save.connect(post_save_user_receiver,sender=User)

