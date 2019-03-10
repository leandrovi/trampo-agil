from django.db import models

# Create your models here.

class Candidatos(models.Model):

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


class Vagas(models.Model):

    cod = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    salario = models.CharField(max_length=200)    

    def __str__(self):
        return self.titulo


