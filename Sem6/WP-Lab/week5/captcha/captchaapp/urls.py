from django.urls import path
from .views import captcha_page, validate_captcha

urlpatterns = [
    path('', captcha_page, name='captcha_page'),  # Renders the CAPTCHA page
    path('validate/', validate_captcha, name='validate_captcha'),  # Handles validation
]
