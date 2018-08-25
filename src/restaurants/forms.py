from django import forms

from .models import RestaurantLocation
from .validators import validate_email,validate_category

class RestaurantLocationCreateForm(forms.ModelForm):
	# Using validators in form fields.But it is better to use them at model fields if you using ModelForm
	# email 		= forms.EmailField(validators=[validate_email])
	# category 	= forms.CharField(required = False,validators=[validate_category])
	class Meta:
		model = RestaurantLocation
		fields = [
			'name',
			'location',
			'category',
			'slug',
		]

	# To show some validation.
	# def clean_name(self):
	# 	name = self.cleaned_data.get('name')
	# 	if name == "Hello":
	# 		raise forms.ValidationError("Not a Valid Name")
	# 	return name

	# To show validatio.
	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	if '.edu' in email:
	# 		raise forms.ValidationError('.edu domain emails are not accpeted')

	# 	return email