from django.shortcuts import render
from .forms import SubForm

# Create your views here.

def home(request):
    context = {}
    form = SubForm(request.POST or None)
    context['form'] = form
    return render(request,'home.html',context)

def display(request):
    context = {}
    subject = 'Mathematics'
    name = 'Disha'
    roll = '16'
    if request.method == "POST":
        loginform  = SubForm(request.POST)
        if loginform.is_valid():
            subject = loginform.cleaned_data['subject']
            name = loginform.cleaned_data['name']
            roll = loginform.cleaned_data['roll']
        else:
            loginform  = SubForm()
    context['subject'] = subject
    context['name'] = name
    context['roll'] = roll
    return render(request,'display.html',context)