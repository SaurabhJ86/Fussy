from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save

"""
While referencing User Model it is better to use AUTH_USER_MODEL as comparted to get_user_model
"""
User = settings.AUTH_USER_MODEL

class Profil(models.Model):
	owner 		= 	models.OneToOneField(User)
	followers 	= 	models.ManyToManyField(User,related_name="ist_following",blank=True)
	activated 	= 	models.BooleanField(default=False)
	timestamp 	= 	models.DateTimeField(auto_now_add=True)
	updated 	=	models.DateTimeField(auto_now=True)


	"""
	Use below instead of self.owner since owner is OneToOneField.
	"""
	def __str__(self):
		return self.owner.username


"""
The below will create a Profil based when a new user is created and also add a default profile to the newly created Profil
This default profil is because the newly created user can have some default data to look otherwise it would look blank.
"""
def user_receiver_profil_signal(sender,instance,created,*args,**kwargs):
	if created:
		profile,is_created 	= Profil.objects.get_or_create(owner=instance)
		# default_profile 	= sender.objects.all()[0]
		default_profile_add = sender.objects.get(pk=1)
		# profile.followers.add(default_profile)
		profile.followers.add(default_profile_add)


post_save.connect(user_receiver_profil_signal,sender=User)