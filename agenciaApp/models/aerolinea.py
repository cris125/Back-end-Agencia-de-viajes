from django.db import models

class Aerolinea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Aerolinea', max_length=50)
    


