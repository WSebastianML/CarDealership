from rest_framework import viewsets
from .models import Ciatt003, Ocxxt004
from django.shortcuts import render
from .serializers import Ciatt003Serializer, Ocxxt004Serializer
from rest_framework.views import APIView
from rest_framework.response import Response

class Ciatt003ViewSet(viewsets.ModelViewSet):
    serializer_class = Ciatt003Serializer

    ## se obtiene el nombre de la division
    def get_queryset(self):
        return Ciatt003.objects.filter(co_tipfila = 'd')

class Ocxxt004ViewSet(viewsets.ModelViewSet):
    serializer_class = Ocxxt004Serializer
    
    def get_queryset(self):
        queryset = Ocxxt004.objects.filter(to_cia='e')
        
        division_seleccionada = self.request.query_params.get('division')
        
        if division_seleccionada:
            queryset = queryset.filter(to_division=division_seleccionada)
            
        return queryset

def compras_home(request):
    return render(request, 'compras/compras_select.html')