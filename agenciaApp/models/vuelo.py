from django.db import models
from .aerolinea import Aerolinea

class Vuelo(models.Model):
    id = models.AutoField(primary_key=True)
    destino = models.CharField('Destino', max_length=50)
    fecha = models.DateTimeField()
    valor = models.DecimalField(decimal_places=3,max_digits=11)
    aerolinea = models.ForeignKey(Aerolinea, related_name='vuelo', on_delete=models.CASCADE)

