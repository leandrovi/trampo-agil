from django.db import models

# Create your models here.

class Candidato(models.Model):

    nome = models.CharField(max_length=200)
    email = models.EmailField()
    carreira = models.CharField(max_length=100)
    senha = models.CharField(max_length=20)
    confirmar_senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Empresa(models.Model):

    nome = models.CharField(max_length=200)
    nome_representante = models.CharField(max_length=200)
    email = models.EmailField()
    carreira = models.CharField(max_length=100)
    senha = models.CharField(max_length=20)
    confirmar_senha = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

