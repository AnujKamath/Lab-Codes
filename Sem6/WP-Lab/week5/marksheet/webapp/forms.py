from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    dob = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(label="Address", widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    contact_number = forms.CharField(label="Contact Number", max_length=15)
    email = forms.EmailField(label="Email ID")
    english_marks = forms.IntegerField(label="Marks in English", min_value=0, max_value=100)
    physics_marks = forms.IntegerField(label="Marks in Physics", min_value=0, max_value=100)
    chemistry_marks = forms.IntegerField(label="Marks in Chemistry", min_value=0, max_value=100)
