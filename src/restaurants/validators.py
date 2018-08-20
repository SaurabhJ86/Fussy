from django.core.exceptions import ValidationError


def validate_email(value):
	email = value
	if ".edu" in email:
		raise ValidationError(".edu domain email address not allowed.")


CATEGORIES = ['Indian','Chinese','American','European','English','Italian','Japanese','East Asian','Lebanese']
def validate_category(value):
	cat = value.capitalize()
	if cat not in CATEGORIES:
		raise ValidationError(f" {value} is not a valid category")