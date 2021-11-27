from rest_framework import routers
from .views import PersonaViewsets
from django.urls import path, include

routers = routers.DefaultRouter()
routers.register('persona', PersonaViewsets)


urlpatterns = [
    path('api/', include(routers.urls)),
]
