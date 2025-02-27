from django.shortcuts import render, redirect
from django.http import HttpResponse

def first_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        subject = request.POST.get('subject')

        request.session['name'] = name
        request.session['roll'] = roll
        request.session['subject'] = subject

        return redirect('second_page')

    return render(request, 'firstPage.html')


def second_page(request):
    name = request.session.get('name', 'Not available')
    roll = request.session.get('roll', 'Not available')
    subject = request.session.get('subject', 'Not available')

    context = {
        'name': name,
        'roll': roll,
        'subject': subject,
    }

    if request.method == 'POST':
        return redirect('first_page')

    return render(request, 'secondPage.html', context)
