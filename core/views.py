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
        pw   = request.POST.get('password')

        try:
            company = Company.objects.get(db_alias=db_alias)

            # Punto 3: inyectar config solo si no existe aún
            if db_alias not in connections.databases:
                connections.databases[db_alias] = {
                    'ENGINE':       company.db_engine,
                    'NAME':         company.db_name,
                    'HOST':         company.db_host,
                    'USER':         '',
                    'PASSWORD':     '',
                    'CONN_MAX_AGE': 0,
                    'TEST':         {'NAME': None},
                    'OPTIONS':      {'MIGRATE': False},
                }
                if company.db_engine == 'django_informixdb':
                    connections.databases[db_alias]['DSN']    = company.db_dsn
                    connections.databases[db_alias]['SERVER'] = company.db_server
                if company.db_port:
                    connections.databases[db_alias]['PORT'] = str(company.db_port)

            conn = connections[db_alias]
            conn.close()

            # Aplica credenciales del usuario actual
            conn.settings_dict['USER']     = user
            conn.settings_dict['PASSWORD'] = pw

            conn.ensure_connection()

            # Punto 1: verificar que la DB conectada coincide con la empresa
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT TRIM(name) FROM sysmaster:sysdatabases "
                    "WHERE is_logging = 1 AND TRIM(name) = ?",
                    [company.db_name]
                )
                row = cursor.fetchone()

            if not row or row[0].lower() != company.db_name.lower():
                conn.close()
                error = "Error de integridad: la base de datos conectada no coincide con la empresa."
                return render(request, 'core/login_informix.html', {'error': error})

            # Punto 2: credenciales específicas por empresa
            request.session[f'user_{company.key}'] = user
            request.session[f'pass_{company.key}'] = pw
            messages.success(request, "Conexión exitosa.")
            return redirect('dashboard')

        except Company.DoesNotExist:
            error = "Empresa no encontrada en la configuración."
            return render(request, 'core/login_informix.html', {'error': error})
        except Exception as e:
            try:
                connections[db_alias].close()
            except Exception:
                pass
            error = f"Credenciales inválidas para {db_alias}."
            return render(request, 'core/login_informix.html', {'error': error})

    return render(request, 'core/login_informix.html')


def dashboard(request):
    company_key = request.session.get('company_key')

    if not company_key or not request.session.get(f'user_{company_key}'):
        return redirect('company_select')

    try:
        company = Company.objects.get(key=company_key)
    except Company.DoesNotExist:
        return redirect('company_select')

    context = {
        'company':  company,
        'db_user':  request.session.get(f'user_{company_key}'),
    }
    return render(request, 'core/dashboard.html', context)