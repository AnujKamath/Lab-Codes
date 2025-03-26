from django.shortcuts import render
from .models import Institute
from .forms import InstituteForm

def institute_list(request):
    selected_institute = None

    if request.method == "POST":
        form = InstituteForm(request.POST)
        if form.is_valid():
            selected_institute = form.cleaned_data["institute"]
    
    else:
        form = InstituteForm()

    return render(request, 'base.html', {'form': form, 'selected_institute': selected_institute})
