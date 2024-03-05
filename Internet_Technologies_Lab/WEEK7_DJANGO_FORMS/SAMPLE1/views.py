from django.shortcuts import render
#from .forms import RegForm 

# creating a home view 
#def home_view(request): 
#	context = {} 
#	form = RegForm(request.POST or None) 
#	context['form'] = form 
#	return render(request, "home.html", context) 
from .forms import GeeksForm
def home_view(request): 
	context = {} 
	form = GeeksForm(request.POST or None) 
	context['form'] = form 
	return render(request, "home.html", context) 



