from agenciaApp.models.vuelo import Vuelo
from rest_framework import serializers

class VueloSerializer(serializers.ModelSerializer):
   class Meta:
       model = Vuelo
       fields = ['id', 'destino', 'fecha', 'valor', 'aerolinea'] 