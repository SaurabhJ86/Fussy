from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

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
	user 		= models.OneToOneField(User)#user.profile
	followers 	= models.ManyToManyField(User,related_name="is_following",blank=True)#user.followers
	# Not Required since the above would do the work for both of them.
	# following 	= models.ManyToManyField(User,related_name="following",blank=True)#user.following
	activated 	= models.BooleanField(default=False)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	objects = ProfileManager()

	def __str__(self):
		return self.user.username


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

