from django.db import connections
from core.db_context import set_db_credentials

class DynamicConnectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'myapp/api/' in request.path and not request.session.get('company_key'):
            from django.shortcuts import redirect
            return redirect('company_select')

        company_key = request.session.get('company_key')
        db_alias    = request.session.get('company_db', 'default')

        # Punto 2: recupera credenciales específicas de esta empresa
        db_user = request.session.get(f'user_{company_key}')
        db_pass = request.session.get(f'pass_{company_key}')

        # Reaplicar credenciales si la conexión existe
        if db_alias != 'default' and db_user and db_pass:
            if db_alias in connections.databases:
                conn = connections[db_alias]
                if conn.settings_dict.get('USER') != db_user:
                    conn.close()
                    conn.settings_dict['USER']     = db_user
                    conn.settings_dict['PASSWORD'] = db_pass

        set_db_credentials(db_alias, db_user, db_pass)
        return self.get_response(request)