# webapp/views.py
from django.shortcuts import render, redirect
from .models import Human
from django.http import JsonResponse

def human_list(request):
    humans = Human.objects.all()
    first_names = [h.first_name for h in humans]
    return render(request, 'human_list.html', {'first_names': first_names})

def get_human_details(request, first_name):
    try:
        human = Human.objects.get(first_name=first_name)
        return JsonResponse({
            'first_name': human.first_name,
            'last_name': human.last_name,
            'phone': human.phone,
            'address': human.address,
            'city': human.city,
        })
    except Human.DoesNotExist:
        return JsonResponse({})

def update_human(request, first_name):
    human = Human.objects.get(first_name=first_name)
    if request.method == 'POST':
        human.last_name = request.POST.get('last_name')
        human.phone = request.POST.get('phone')
        human.address = request.POST.get('address')
        human.city = request.POST.get('city')
        human.save()
        return redirect('human_list')

def delete_human(request, first_name):
    human = Human.objects.get(first_name=first_name)
    human.delete()
    return redirect('human_list')
