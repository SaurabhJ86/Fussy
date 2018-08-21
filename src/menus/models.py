from django.conf import settings
from django.db import models

# Create your models here.
from restaurants.models import RestaurantLocation

User = settings.AUTH_USER_MODEL
class Item(models.Model):
	# Menu Item Association Info
	user 		= models.ForeignKey(User)
	restaurant 	= models.ForeignKey(RestaurantLocation)
	# Menu Item Info
	name 		= models.CharField(max_length=120)
	contents 	= models.TextField(help_text='Separate each item by comma')
	exclude 	= models.TextField(blank=True, null=True,help_text='Separate each item by comma')
	public 		= models.BooleanField(default=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-updated','-timestamp']


	def get_contents(self):
		return self.contents.split(",")

	def get_exclude(self):
		return self.exclude.split(",")
