from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    message = None
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            message = f"Thanks {student_name} for your feedback."
    else:
        form = FeedbackForm()

    return render(request, 'base.html', {'form': form, 'message': message})
