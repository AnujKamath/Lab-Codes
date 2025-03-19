from django.shortcuts import render, redirect
from .forms import OrderForm

PRICE_LIST = {
    'Mobile': 10000,
    'Laptop': 50000,
}

def order_view(request):
    if request.GET.get('new_order'):
        request.session.pop('order_data', None)
        return redirect('order')

    order_data = request.session.get('order_data', None)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            request.session['order_data'] = form.cleaned_data
            return redirect('order')  
    else:
        form = OrderForm()

    total_price = None
    if order_data:
        total_price = sum(PRICE_LIST[item] * order_data['quantity'] for item in order_data['items'])

    return render(request, 'base.html', {'form': form, 'order': order_data, 'total_price': total_price})
