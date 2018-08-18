from django.db import models
from django.db.models.signals import pre_save,post_save

from .utils import unique_slug_generator
from .validators import validate_category
# Create your models here.


class RestaurantLocation(models.Model):

	name 		= models.CharField(max_length = 120)
	location 	= models.CharField(max_length = 120, null=True, blank=True)
	category 	= models.CharField(max_length = 120, null=True, blank=True,validators=[validate_category])
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	slug 		= models.SlugField(null=True,blank=True)


	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name

# This signal will be used to fill the slug field right before it is being saved using the slug generator.
def rl_pre_save_receiver(sender,instance,*args,**kwargs):
	# The below is checking whether the first letter is capitalized, if not then saved the capitalized version.
	if not instance.category.istitle():
		instance.category = instance.category.capitalize()
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


# Connecting the pre_save signal between the receiver(rl_pre_save_receiver) and the sender(RestaurantLocation)
pre_save.connect(rl_pre_save_receiver,RestaurantLocation)
	