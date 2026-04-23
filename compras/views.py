from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Ocxxt013
from . import serializers
from . import services
import json

class Ciatt003ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Ciatt003Serializer

    def get_queryset(self):
        return services.get_divisiones()

class Ocxxt004ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Ocxxt004Serializer

    def get_queryset(self):
        division = self.request.query_params.get('division')
        return services.get_tipos_compra(division=division)

class Ocxxt006ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Ocxxt006Serializer

    def get_queryset(self):
        return services.get_solicitantes()

class Coat007ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Coat007Serializer

    def get_queryset(self):
        return services.get_tipos_credito()

class Ocxxt013ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.Ocxxt013Serializer

    def get_queryset(self):
        ruc = self.request.query_params.get('rucprov')
        if ruc:
            return services.get_cuentas_por_ruc(ruc)
        return Ocxxt013.objects.none() 

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return JsonResponse({'ncuentaprov': response.data})

def compras_home(request):
    return render(request, 'compras/compras_select.html')