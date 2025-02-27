from django import forms

class CarForm(forms.Form):
    CAR_BRANDS = [
        ('Mahindra', 'Mahindra'),
        ('Tata', 'Tata'),
        ('Volkswagon', 'Volkswagon'),
    ]
    car_brand = forms.ChoiceField(label='Car Manufacturer', choices=CAR_BRANDS)
    car_model = forms.CharField(label='Car Model Name', max_length=100)
