from rest_framework import serializers
from .models import Cgrta004

class Cgrta004Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cgrta004
        fields = '__all__'
