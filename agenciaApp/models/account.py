from django.db import models
from .user import User
from .reserva import Reserva
from .factura import Factura

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)
    reservas = models.ForeignKey(Reserva, related_name='account', on_delete=models.CASCADE, null = True )
    facturas = models.ForeignKey(Factura, related_name='account', on_delete=models.CASCADE, null = True )