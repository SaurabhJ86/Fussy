from django import forms

from .models import Item

from restaurants.models import RestaurantLocation

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = [
		'restaurant',
		'name',
		'contents',
		'exclude',
		'public'
		]

	def __init__(self,user=None,*args,**kwargs):
		# a = kwargs.pop('text',None)
		# print(a)
		super(ItemForm,self).__init__(*args,**kwargs)
		# This will return a filter queryset , otherwise the returned queryset would be "RestaurantLocation.objects.all()"
		self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner = user)#.exclude(item__isnull=False)