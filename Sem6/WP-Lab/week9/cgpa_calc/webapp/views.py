from django.shortcuts import render
from .forms import CGPACalculatorForm

def home(request):
    if request.method == 'POST':
        form = CGPACalculatorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            total_marks = form.cleaned_data['total_marks']
            cgpa = total_marks / 50
            request.session['name'] = name
            request.session['cgpa'] = cgpa
            return render(request, 'result.html', {'name': name, 'cgpa': cgpa})
    else:
        form = CGPACalculatorForm()
    return render(request, 'home.html', {'form': form})

def result(request):
    name = request.session.get('name', 'Guest')
    cgpa = request.session.get('cgpa', 0)
    return render(request, 'result.html', {'name': name, 'cgpa': cgpa})
