from rest_framework import serializers
from .models import Ciatt003, Ocxxt004, Ocxxt006, Coat007

class Ciatt003Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ciatt003
        fields = '__all__'

class Ocxxt004Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ocxxt004
        fields = '__all__'

class Ocxxt006Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ocxxt006
        fields = '__all__'

class Coat007Serializer(serializers.ModelSerializer):
    class Meta:
        model = Coat007
        fields = '__all__'