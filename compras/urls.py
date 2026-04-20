from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Ciatt003ViewSet, Ocxxt004ViewSet

router = DefaultRouter()
#router.register(r'tipos-compra', Ocxxt004ViewSet, basename='ocxxt004')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tipos_compra/', Ciatt003ViewSet.as_view(), name='tipos_compra'),
]