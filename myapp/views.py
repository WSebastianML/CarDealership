from rest_framework import viewsets
from .models import Cgrta004
from django.shortcuts import render
from .serializers import Cgrta004Serializer
from rest_framework.views import APIView
from rest_framework.response import Response

class Cgrta004ViewSet(APIView):
    def get(self, request):
        # El router ya sabe qué DB usar gracias al middleware
        queryset = Cgrta004.objects.all() 
        serializer = Cgrta004Serializer(queryset, many=True)
        return Response(serializer.data)