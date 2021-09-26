from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)


class Evento(models.Model):
    dia = models.DateField(auto_now=False, auto_now_add=False)
    local = models.CharField(max_length=200)


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    data = models.DateField(auto_now=False, auto_now_add=False)
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)


class Reserva(models.Model):
    comprador = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)

