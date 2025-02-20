from django.shortcuts import render

def calculator(request):
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'sub':
                result = num1 - num2
            elif operation == 'mul':
                result = num1 * num2
            elif operation == 'div':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Cannot divide by zero'
            else:
                result = 'Invalid operation'

        except ValueError:
            result = 'Please enter valid numbers'
        
        return render(request, 'base.html', {'result': result})

    return render(request, 'base.html')
