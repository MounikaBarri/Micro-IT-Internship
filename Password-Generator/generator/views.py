from django.shortcuts import render, redirect
from .utils.password_generator import generate_password

def password_requirements(request):
    if request.method == 'POST':
        request.session['password_params'] = {
            'length': int(request.POST.get('length', 12)),
            'uppercase': 'uppercase' in request.POST,
            'lowercase': 'lowercase' in request.POST,
            'digits': 'digits' in request.POST,
            'special': 'special' in request.POST
        }
        return redirect('password_result')
    
    # Default values for first visit
    return render(request, 'generator/requirements.html')

def password_result(request):
    params = request.session.get('password_params', {
        'length': 12,
        'uppercase': True,
        'lowercase': True,
        'digits': True,
        'special': True
    })
    
    try:
        password = generate_password(**params)
    except ValueError as e:
        return redirect('password_requirements')
    
    return render(request, 'generator/result.html', {
        'password': password,
        'params': params  # Pass parameters to show what was selected
    })