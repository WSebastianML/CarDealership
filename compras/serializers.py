from rest_framework import serializers
from .models import Ciatt003, Ocxxt004

class Ciatt003Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ciatt003
        fields = '__all__'

class Ocxxt004Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ocxxt004
        fields = '__all__'