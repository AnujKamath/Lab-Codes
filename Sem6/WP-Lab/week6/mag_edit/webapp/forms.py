from django import forms

class MagazineForm(forms.Form):
    heading = forms.CharField(max_length=100)
    bg_image = forms.ImageField()  
    bg_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    font_size = forms.IntegerField(min_value=10, max_value=100)
    font_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
