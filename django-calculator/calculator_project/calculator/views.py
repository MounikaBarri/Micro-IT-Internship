from django.shortcuts import render
from django.http import JsonResponse
from .models import Calculation
import json

def calculator_view(request):
    return render(request, 'calculator/calculator.html')

def calculate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            expression = data.get('expression')
            
            # Basic security check - only allow certain characters
            allowed_chars = set('0123456789+-*/.%() ')
            if not all(c in allowed_chars for c in expression):
                return JsonResponse({'error': 'Invalid characters in expression'}, status=400)
            
            result = str(eval(expression))
            
            # Save to database
            Calculation.objects.create(expression=expression, result=result)
            
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_history(request):
    calculations = Calculation.objects.all().order_by('-created_at')[:10]
    history = [{'expression': calc.expression, 'result': calc.result} for calc in calculations]
    return JsonResponse({'history': history})