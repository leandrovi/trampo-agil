from django.db import models
from site_trampo_agil.models import Empresa

# Create your models here.
class Vaga(models.Model):
    cod = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    salario = models.CharField(max_length=200)    

    def __str__(self):
        return self.titulo