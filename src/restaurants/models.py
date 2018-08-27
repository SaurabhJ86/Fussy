from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save,post_save

from .utils import unique_slug_generator
from .validators import validate_category


User = settings.AUTH_USER_MODEL


class RestaurantLocationQuerySet(models.QuerySet):
	def search(self,query):#This is like RestaurantLocation.objects.filter(owner=user).search(query)
		if query:
			# This will make sure that no space is passed to the query
			query = query.strip()
			return self.filter(
							Q(name__icontains=query)|
							Q(location__icontains=query)|
							Q(category__icontains=query)|
							Q(item__name__icontains=query)|
							Q(item__contents__icontains=query)
							).distinct()
		else:
			return self

class RestaurantLocationManager(models.Manager):
	def get_queryset(self):
		return RestaurantLocationQuerySet(self.model,using=self._db)
	# def search(self,user,query):
	def search(self,query): #This is like RestaurantLocation.objects.search(query)
		# In this case it will do RestaurantLocation.objects.all() and the result QuerySet it will pass to search() QuerySet created above.
		return self.get_queryset().search(query)
		# return self.get_queryset().filter(name__icontains=query,owner=user)


class RestaurantLocation(models.Model):
	owner 		= models.ForeignKey(User)
	name 		= models.CharField(max_length = 120)
	location 	= models.CharField(max_length = 120, null=True, blank=True)
	category 	= models.CharField(max_length = 120, null=True, blank=True,validators=[validate_category])
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	slug 		= models.SlugField(null=True,blank=True)

	objects = RestaurantLocationManager()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants:detail',kwargs={"slug":self.slug})

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
	