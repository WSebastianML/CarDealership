from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import Ciatt003Serializer, Ocxxt004Serializer, Ocxxt006Serializer, Coat007Serializer
from . import services
import json

class Ciatt003ViewSet(viewsets.ModelViewSet):
    serializer_class = Ciatt003Serializer

    def get_queryset(self):
        return services.get_divisiones()

class Ocxxt004ViewSet(viewsets.ModelViewSet):
    serializer_class = Ocxxt004Serializer
    
    def get_queryset(self):
        division = self.request.query_params.get('division')
        return services.get_tipos_compra(division=division)

class Ocxxt006ViewSet(viewsets.ModelViewSet):
    serializer_class = Ocxxt006Serializer
    
    def get_queryset(self):
        return services.get_solicitantes()

class Coat007ViewSet(viewsets.ModelViewSet):
    serializer_class = Coat007Serializer

    def get_queryset(self):
        return services.get_tipos_credito()

def compras_home(request):
    return render(request, 'compras/compras_select.html')