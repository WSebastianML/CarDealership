from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'divisiones', views.Ciatt003ViewSet, basename='ciatt003')
router.register(r'tipos-compra', views.Ocxxt004ViewSet, basename='ocxxt004')
router.register(r'solicitantes', views.Ocxxt006ViewSet, basename='ocxxt006')
router.register(r'tipos-credito', views.Coat007ViewSet, basename='coat007')
router.register(r'cuentas-proveedor', views.Ocxxt013ViewSet, basename='ocxxt013')

urlpatterns = [
    path('api/', include(router.urls)),
    #path('api/tipos_compra/', Ciatt003ViewSet.as_view(), name='tipos_compra'),
    path('api/gestion/', views.compras_home, name='compras_view'),
]