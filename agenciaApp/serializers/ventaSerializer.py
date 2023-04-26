from agenciaApp.models.venta import Venta
from rest_framework import serializers

class VentaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Venta
       fields = ['id', 'vuelo'] 
def to_representation(self, obj):
      Venta = Venta.objects.get(id=obj.id)
      
      return {
        'id': Venta.id,
        'Vuelo': Venta.vuelo,
        
    }