from django.shortcuts import render
from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerializers


# Create your views here.


class PersonaViewsets(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializers_class = PersonaSerializers
