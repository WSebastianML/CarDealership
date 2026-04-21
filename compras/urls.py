from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Ciatt003ViewSet, Ocxxt004ViewSet, Ocxxt006ViewSet, compras_home

router = DefaultRouter()
router.register(r'divisiones', Ciatt003ViewSet, basename='ciatt003')
router.register(r'tipos-compra', Ocxxt004ViewSet, basename='ocxxt004')
router.register(r'solicitantes', Ocxxt006ViewSet, basename='ocxxt006')

urlpatterns = [
    path('api/', include(router.urls)),
    #path('api/tipos_compra/', Ciatt003ViewSet.as_view(), name='tipos_compra'),
    path('api/gestion/', compras_home, name='compras_view'),
]