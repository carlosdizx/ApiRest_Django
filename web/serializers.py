from django.db.models import Model
from rest_framework import serializers
from .models import Persona


class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        Model = Persona
        fields = '__all__'
