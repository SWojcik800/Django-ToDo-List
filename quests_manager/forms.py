from django import forms
from django.forms import ModelForm
from .models import Quest

class QuestCreateForm(forms.ModelForm):
     class Meta:
         model = Quest
         fields = ['title', 'body']
         widgets = {
         'title' : forms.TextInput(attrs={'class': "form-control", 'placeholder' : 'Quest title'}),
         'body' : forms.TextInput(attrs={'class': "form-control", 'type' : 'textarea', 'placeholder' : 'Quest body'}),
         }
