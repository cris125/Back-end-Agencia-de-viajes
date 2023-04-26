from django.db import models
from .user import User

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    vuelo = models.ForeignKey(User, related_name='vuelo', on_delete=models.CASCADE)
    
    


