from django.shortcuts import render
from .forms import Publisherf, Bookf, Authorf
from .models import Publisher, Book, Author

def home(req):
	return render(req, '')

# Create your views here.
