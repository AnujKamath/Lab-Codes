from django.shortcuts import render 
from django.http import HttpResponse 
from .forms import StudentForm

def index(request):
    return HttpResponse("<H2>HEY! Welcome to Edureka! </H2>")


def student_details(request):
    total_percentage = None
    student_info = None
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            address = form.cleaned_data['address']
            contact_number = form.cleaned_data['contact_number']
            email = form.cleaned_data['email']
            english_marks = form.cleaned_data['english_marks']
            physics_marks = form.cleaned_data['physics_marks']
            chemistry_marks = form.cleaned_data['chemistry_marks']
            
            total_marks = english_marks + physics_marks + chemistry_marks
            percentage = (total_marks / 300) * 100
            total_percentage = round(percentage, 2)  
            
            student_info = {
                'name': name,
                'dob': dob,
                'address': address,
                'contact_number': contact_number,
                'email': email,
                'english_marks': english_marks,
                'physics_marks': physics_marks,
                'chemistry_marks': chemistry_marks,
                'total_marks': total_marks,
                'percentage': total_percentage,
            }
    else:
        form = StudentForm()
    
    return render(request, 'base.html', {'form': form, 'student_info': student_info, 'total_percentage': total_percentage})
