from django.shortcuts import render, redirect
from .models import Works, Lives
from .forms import WorksForm, CompanyQueryForm


def insert_data(request):
    if request.method == 'POST':
        form = WorksForm(request.POST)  
        if form.is_valid():
            works_entry = form.save()

            lives_entry = Lives(person_name=works_entry.person_name, street="Default Street", city="Default City")
            lives_entry.save()

            return redirect('insert_data')  

    else:
        form = WorksForm() 

    return render(request, 'webapp/insert_data.html', {'form': form})


def company_query(request):
    people = []
    if request.method == 'POST':
        form = CompanyQueryForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            print(f"Querying for company: {company_name}")  

            works = Works.objects.filter(company_name=company_name)
            print(f"Found {works.count()} records in Works for company {company_name}")  
            
            for work in works:
                print(f"Checking city for: {work.person_name}")  
                # Get the city they live in
                city = Lives.objects.filter(person_name=work.person_name).first()
                if city:
                    print(f"Found city: {city.city} for {work.person_name}")
                    people.append({
                        'person_name': work.person_name,
                        'city': city.city
                    })
                else:
                    print(f"No city found for {work.person_name}")  

    else:
        form = CompanyQueryForm()

    return render(request, 'webapp/company_query.html', {'form': form, 'people': people})
