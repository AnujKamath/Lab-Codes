from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CarForm

def car_form(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car_brand = form.cleaned_data['car_brand']
            car_model = form.cleaned_data['car_model']
            return redirect(f'/result/?car_brand={car_brand}&car_model={car_model}')
    else:
        form = CarForm()

    return render(request, 'base.html', {'form': form})


def result(request):
    car_brand = request.GET.get('car_brand', '')
    car_model = request.GET.get('car_model', '')
    return render(request, 'result.html', {'car_brand': car_brand, 'car_model': car_model})
