from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label="User Name")
    password = forms.CharField(widget=forms.PasswordInput, required=False, label="Password")
    email = forms.EmailField(required=False, label="Email ID")
    contact_number = forms.CharField(max_length=15, required=False, label="Contact Number")
