from .models import Author, Publisher, Book
from django import forms

class Authorf(forms.Form):
	fname = forms.CharField()
	lname = forms.CharField()
	email = forms.CharField(
		max_length=255,
		unique=True,
		widget=forms.EmailInput())

class Publisherf(forms.Form):
	name = forms.CharField()
	addr = forms.CharField()
	city = forms.CharField()
	state = forms.CharField()
	country = forms.CharField()
	website = forms.URLField()

class Bookf(forms.Form): 
	title = forms.CharField() 
	date = forms.DateField() 
	authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all()) 
	publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())

