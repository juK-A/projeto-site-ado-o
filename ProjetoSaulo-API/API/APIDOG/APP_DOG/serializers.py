from rest_framework import serializers
from .models import Adotante,Dog

class AdotanteSerializer(serializers.ModelSerializer): # Conversor para JSON (MODEL -> JSON)
    class Meta:
        model = Adotante
        fields = '__all__' 


class DogSerializer(serializers.ModelSerializer): # Conversor para JSON (MODEL -> JSON)
    class Meta:
        model = Dog
        fields = '__all__' 