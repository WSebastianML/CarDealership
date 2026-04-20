from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Cgrta004ViewSet

router = DefaultRouter()
#router.register(r'ejemplo', Ciatt003ViewSet, basename='ciatt003')
#router.register(r'tipos-compra', Ocxxt004ViewSet, basename='ocxxt004')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/cuentas/', Cgrta004ViewSet.as_view(), name='cuentas_html'),
    #path('ejemplo/', ejemplo_html, name='ejemplo_html'),
    #path('conexiones/', Cgrta004ViewSet.as_view(), name = 'conexiones'),
]