from django.db import models
from datetime import date, datetime

class Realtor(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='photos/%Y/%m/%d/')
    descrição = models.TextField(blank=True)
    celular = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    mais_vendido = models.BooleanField(default=False)
    data_contratacao = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome 
