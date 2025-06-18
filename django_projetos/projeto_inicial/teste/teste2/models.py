from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class BancoModel(models.Model):
    email = models.EmailField(max_length=255, unique=True)  # Melhor usar EmailField
    senha = models.CharField(max_length=128)  # Para armazenar hash
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=20)
    criacaodeconta = models.DateField(auto_now_add=True)
    
    def set_password(self, raw_password):
        self.senha = make_password(raw_password)
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)
    