from django.db import models
from .user import User

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    valor_reserva = models.DecimalField(decimal_places=3,max_digits=11)
    destino_reserva = models.CharField('Destino', max_length=50)
    user = models.ForeignKey(User, related_name='reserva', on_delete=models.CASCADE)
    
