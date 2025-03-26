from django import forms
from .models import Institute

class InstituteForm(forms.Form):
    institute = forms.ModelChoiceField(queryset=Institute.objects.all(), empty_label="Select an Institute")
