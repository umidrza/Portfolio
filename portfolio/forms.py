from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta: 
        model = Portfolio
        fields = ['name', 'surname', 'address', 'number', 'education', 'experiences', 'skills', 
                  'hobbies', 'languages', 'social_accounts']