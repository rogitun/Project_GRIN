from django import forms
from django.forms import ModelForm
from .models import *
from django import forms

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body']
        
        labels = {
            'body':'Comment'
        }