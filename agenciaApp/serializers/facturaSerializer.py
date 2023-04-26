from agenciaApp.models.factura import Factura
from rest_framework import serializers

class FacturaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Factura
       fields = ['id', 'fecha', 'user', 'venta', 'producto', 'valor_producto'] 