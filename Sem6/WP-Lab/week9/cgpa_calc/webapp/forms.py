from django import forms

class CGPACalculatorForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    total_marks = forms.IntegerField(label="Total Marks")
