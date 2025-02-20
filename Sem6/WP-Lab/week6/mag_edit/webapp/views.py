from django.shortcuts import render
from .forms import MagazineForm
from django.conf import settings
import os

def magazine_editor(request):
    if request.method == 'POST':
        form = MagazineForm(request.POST, request.FILES)  # Include request.FILES for image upload
        if form.is_valid():
            heading = form.cleaned_data['heading']
            bg_image = form.cleaned_data['bg_image']  # This will be the uploaded image file
            bg_color = form.cleaned_data['bg_color']
            font_size = form.cleaned_data['font_size']
            font_color = form.cleaned_data['font_color']

            # Generate the URL for the uploaded image
            image_url = os.path.join(settings.MEDIA_URL, bg_image.name)
            
            # Pass the data to the template
            return render(request, 'magazine.html', {
                'heading': heading,
                'bg_image': image_url,
                'bg_color': bg_color,
                'font_size': font_size,
                'font_color': font_color
            })
    else:
        form = MagazineForm()

    return render(request, 'base.html', {'form': form})


def magazine_result(request):
    return render(request, 'magazine.html', {
        'heading': 'Magazine Title',  # You can pass the real data from the form if needed
        'bg_image': '/media/images/sample.jpg',  # Use actual image path from media
        'bg_color': '#FFFFFF',  # Example background color
        'font_size': 30,  # Example font size
        'font_color': '#000000',  # Example font color
    })
