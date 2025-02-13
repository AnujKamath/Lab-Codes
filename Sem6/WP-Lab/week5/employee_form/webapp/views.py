from django.shortcuts import render 
from django.http import HttpResponse 
from .forms import EmployeeForm
from datetime import date,datetime

def index(request):
    return HttpResponse("<H2>HEY! Welcome to Edureka! </H2>")

def employee_details(request):
    result = None
    employee_info = None
    
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            doj = form.cleaned_data['doj']

            today = date.today()
            try:
                date_of_joining = datetime.strptime(doj, "%d-%m-%Y").date()
            except ValueError:
                date_of_joining = None 

            difference_in_years = (today - date_of_joining).days / 365.25  # Dividing by 365.25 accounts for leap years

            if difference_in_years > 5:
                result = "Yes"
            else:
                result = "No"

            # year = int(year)
            # month = int(month)
            # date1 = int(date1)
                        
            employee_info = {
                'doj':doj,
            }
    else:
        form = EmployeeForm()
    
    return render(request, 'base.html', {'form': form, 'employee_info': employee_info, 'result': result})
