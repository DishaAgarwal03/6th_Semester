from django.db import models

# Create your models here.
'''author table has a first name, a last name and an email address. 
A publisher table has a name, a street address, a city, a state/ province, a country, and a Web site. 
A book table has a title and a publication date. It also has one or more authors (a many-to-many relationship 
with authors) and a single publisher (a one-to-many relationship - aka foreign 
key - to publishers). 
Design a form which populates and retrieves the information from the above database using Django.'''

class Author(models.Model):
	fname = models.CharField()
	lname = models.CharField()
	email = models.CharField(
		max_length=255,
		unique=True,
		widget=models.EmailInput())

class Publisher(models.Model):
	name = models.CharField()
	addr = models.CharField()
	city = models.CharField()
	state = models.CharField()
	country = models.CharField()
	website = models.URLField()

class Book(models.Model):
	title = models.CharField()
	date = models.DateField(auto_now_add=True)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

