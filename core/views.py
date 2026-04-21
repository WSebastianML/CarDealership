from django.shortcuts import render
from django.db import connections, OperationalError
from django.contrib import messages 
from django.shortcuts import render, redirect
from .models import Company


def company_select(request):

    companies = Company.objects.filter(activa = True)

    if request.method == 'POST':
        company_key = request.POST.get('company')

        try:
            company = Company.objects.get(key=company_key, activa=True)
            request.session['company_key']  = company.key
            request.session['company_db']   = company.db_alias
            request.session['company_name'] = company.name
            return redirect('company_login')

        except Company.DoesNotExist:
            pass

    return render(request, 'core/company_select.html', {'companies': companies})

def company_login(request):

    db_alias = request.session.get('company_db')

    if not db_alias:
        return redirect('company_select')

    if request.method == 'POST':
        user = request.POST.get('username')
        pw = request.POST.get('password')


        try:
            company = Company.objects.get(db_alias=db_alias)
            conn = connections[db_alias]

            conn.settings_dict['USER']     = user
            conn.settings_dict['PASSWORD'] = pw

            if company.db_engine == 'django_informixdb':
                conn.settings_dict['DSN']     = company.db_dsn
                conn.settings_dict['SERVER'] = company.db_server

            conn.settings_dict['HOST']     = company.db_host            
            conn.settings_dict['NAME']     = company.db_name

            if company.db_port:
                conn.settings_dict['PORT'] = str(company.db_port)


            conn.close()
            conn.ensure_connection()

            request.session['db_user'] = user
            request.session['db_pass'] = pw
            messages.success(request, "Conexión exitosa.")
            return redirect('dashboard')

        except Company.DoesNotExist:
            error = "Empresa no encontrada en la configuración."
            return render(request, 'core/login_informix.html', {'error': error})
        except OperationalError as e:
            error = f"Credenciales inválidas para {db_alias}."
            return render(request, 'core/login_informix.html', {'error': error})

    return render(request, 'core/login_informix.html')


def dashboard(request):
    # Recuperamos la clave de la empresa de la sesión
    company_key = request.session.get('company_key')
    
    # Si no hay empresa o no hay usuario logueado en la DB, redirigir
    if not company_key or not request.session.get('db_user'):
        return redirect('company_select')
    
    try:
        company = Company.objects.get(key=company_key)  # ← desde SQLite
    except Company.DoesNotExist:
        return redirect('company_select')

    context = {
        'company': company,
        'db_user': request.session.get('db_user')
    }
    return render(request, 'core/dashboard.html', context)
