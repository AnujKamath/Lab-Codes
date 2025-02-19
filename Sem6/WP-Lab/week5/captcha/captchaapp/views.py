import random
import string
from django.shortcuts import render
from django.http import JsonResponse

def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

def captcha_page(request):
    request.session['captcha'] = generate_captcha()
    request.session['attempts'] = 0
    return render(request, 'captcha.html', {'captcha': request.session['captcha']})

def validate_captcha(request):
    if request.method == "POST":
        user_input = request.POST.get('captcha_input', '').strip()
        if request.session.get('attempts', 0) >= 3:
            return JsonResponse({'status': 'disabled', 'message': '⚠️ Too many failed attempts.'})

        if user_input == request.session.get('captcha', ''):
            return JsonResponse({'status': 'success', 'message': '✅ Captcha Matched!'})

        request.session['attempts'] += 1
        return JsonResponse({'status': 'error', 'message': f'❌ Incorrect! {3 - request.session["attempts"]} attempts left.'})
