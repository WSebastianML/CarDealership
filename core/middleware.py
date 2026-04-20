# core/middleware.py actualizado
from django.shortcuts import redirect
from core.db_context import set_db_credentials

class DynamicConnectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Bloqueo de seguridad: Si intenta ir a la API sin usuario, fuera.
        if 'myapp/api/' in request.path and not request.session.get('db_user'):
            return redirect('company_select')

        db_alias = request.session.get('company_db', 'default')
        db_user = request.session.get('db_user')
        db_pass = request.session.get('db_pass')

        # 2. Seteamos el hilo para el Router
        set_db_credentials(db_alias, db_user, db_pass)

        response = self.get_response(request)
        return response
