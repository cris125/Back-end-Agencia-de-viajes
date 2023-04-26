from agenciaApp.models.reserva import Reserva
from rest_framework import serializers
from agenciaApp.models.reserva import Reserva

class ReservaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Reserva
       fields = ['id', 'fecha', 'user', 'valor_reserva', 'destino_reserva'] 
def to_representation(self, obj):
      Reserva = Reserva.objects.get(id=obj.id)
      
      return {
        'id': Reserva.id,
        'fecha': Reserva.fecha,
        'user': Reserva.user_id,
        'valor_reserva': Reserva.valor_reserva,
        'destino_reserva': Reserva.destino_reserva,
    }