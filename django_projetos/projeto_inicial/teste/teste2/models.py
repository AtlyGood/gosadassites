from django.db import models

# Create your models here.
class BancoModel(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=20)
    criacaodeconta = models.DateField(auto_now_add=True)
    
    