from django.db import models
from .user import User
from .venta import Venta

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    user = models.ForeignKey(User, related_name='factura', on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, related_name='factura', on_delete=models.CASCADE)
    producto = models.CharField('Producto', max_length = 50)
    valor_producto = models.DecimalField(decimal_places=3,max_digits=11)
