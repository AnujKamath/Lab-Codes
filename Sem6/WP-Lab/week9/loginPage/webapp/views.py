from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            contact_number = form.cleaned_data['contact_number']
            request.session['username'] = username
            request.session['email'] = email
            request.session['contact_number'] = contact_number
            return HttpResponseRedirect(reverse('success'))
    else:
        form = RegisterForm()

    return render(request, 'register_page.html', {'form': form})

def success_view(request):
    username = request.session.get('username')
    email = request.session.get('email')
    contact_number = request.session.get('contact_number')
    return render(request, 'success_page.html', {
        'username': username,
        'email': email,
        'contact_number': contact_number,
    })
