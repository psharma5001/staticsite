from django import forms
from .models import *


class WebsiteForm(forms.ModelForm):

    class Meta:
        model = Website
        fields = ('title','summary')

class PageForm(forms.ModelForm): 
    class Meta:
        model = Page
        fields = ('filename','text')
