from rest_framework import serializers
from . import models

class Ciatt003Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ciatt003
        fields = '__all__'

class Ocxxt004Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ocxxt004
        fields = '__all__'

class Ocxxt006Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ocxxt006
        fields = '__all__'

class Coat007Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coat007
        fields = '__all__'

class Ocxxt013Serializer(serializers.ModelSerializer):
    ct_cuenta = serializers.ReadOnlyField(source='mc_cuenta.ct_cuenta')
    ct_descripcion = serializers.ReadOnlyField(source='mc_cuenta.ct_descripcion')

    class Meta:
        model = models.Ocxxt013
        fields = '__all__' 