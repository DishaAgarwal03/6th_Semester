from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubForm
#from .forms import DisplayForm

def first_page(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['roll'] = form.cleaned_data['roll']
            request.session['subject'] = form.cleaned_data['subject']
            return redirect('second_page')
    else:
        form = SubForm()
    return render(request, 'first_page.html', {'form': form})

def second_page(request):
    if request.method == 'POST':
        return redirect('first_page')
    else:
        #form = DisplayForm(initial={'label_text': f"Name: {request.session.get('name')} | Roll: {request.session.get('roll')} | Subject: {request.session.get('subject')}"})
        name = request.session.get('name')
        roll = request.session.get('roll')
        subject = request.session.get('subject')
        return render(request, 'second_page.html', {'name': name, 'roll': roll, 'subject':subject})
    #return render(request, 'second_page.html', {'form': form})
