from django.shortcuts import render
from django.db import connections, OperationalError
from django.contrib import messages 
from django.shortcuts import render, redirect

COMPANIES = {
    'ecuawagen': {
        'name': 'Ecuawagen',
        'db': 'ecuawagen',
        'logo': '/static/ecuawagen.png',
    },
    'germanmoto': {
        'name': 'GermanMoto',
        'db': 'germanmoto',
        'logo': '/static/germanmotors.png',
    }
}

def company_select(request):
    if request.method == 'POST':
        company_key = request.POST.get('company')
        if company_key in COMPANIES:
            request.session['company_key'] = company_key              
            request.session['company_db']   = COMPANIES[company_key]['db']
            request.session['company_name'] = COMPANIES[company_key]['name']
            return redirect('company_login')

    return render(request, 'core/company_select.html', {'companies': COMPANIES})

def company_login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pw = request.POST.get('password')
        db_alias = request.session.get('company_db')

        if not db_alias:
            return redirect('company_select')

        # --- PRUEBA DE CONEXIÓN DINÁMICA ---
        try:
            # 1. Obtenemos el objeto de conexión configurado en settings.py
            conn = connections[db_alias]

            # 2. Inyectamos temporalmente las credenciales del formulario
            # Guardamos las originales para restaurar si es necesario
            original_user = conn.settings_dict.get('USER')
            original_pass = conn.settings_dict.get('PASSWORD')
            
            conn.settings_dict['USER'] = user
            conn.settings_dict['PASSWORD'] = pw

            # 3. Forzamos el cierre de cualquier conexión vieja e intentamos abrir una nueva
            conn.close()
            conn.ensure_connection() 

            # SI LLEGA AQUÍ, LA CONEXIÓN FUE EXITOSA
            request.session['db_user'] = user
            request.session['db_pass'] = pw
            messages.success(request, "Conexión exitosa a Informix.")
            return redirect('dashboard')

        except OperationalError as e:
            # SI FALLA (Usuario/Password incorrectos, etc.)
            # Restauramos valores (opcional)
            conn.settings_dict['USER'] = original_user
            conn.settings_dict['PASSWORD'] = original_pass
            
            error_msg = f"Error de autenticación en {db_alias}: Credenciales inválidas."
            return render(request, 'core/login_informix.html', {'error': error_msg})

    return render(request, 'core/login_informix.html')


def dashboard(request):
    # Recuperamos la clave de la empresa de la sesión
    company_key = request.session.get('company_key')
    
    # Si no hay empresa o no hay usuario logueado en la DB, redirigir
    if not company_key or not request.session.get('db_user'):
        return redirect('company_select')
    
    context = {
        'company': COMPANIES.get(company_key),
        'db_user': request.session.get('db_user')
    }
    return render(request, 'core/dashboard.html', context)
