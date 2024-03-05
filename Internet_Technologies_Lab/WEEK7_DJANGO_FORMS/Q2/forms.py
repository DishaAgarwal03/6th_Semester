from django import forms

class SubForm(forms.Form):
    subs=(
        ('Mathematics','Mathematics'),
        ('Physics','Physics'),
        ('Computer Science','Computer Science'),
        )
    name = forms.CharField()
    roll = forms.CharField()
    subject = forms.ChoiceField(widget=forms.Select,choices=subs)
