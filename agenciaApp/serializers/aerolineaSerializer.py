from agenciaApp.models.aerolinea import Aerolinea
from rest_framework import serializers

class AerolineaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Aerolinea
       fields = ['id', 'nombre'] 