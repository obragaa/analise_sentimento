from django.db import models
from django.contrib.auth.models import AbstractUser

class Frases(models.Model):
    OPCOES_CATEGORIA = [
        ("POSITIVO", "Positivo"),
        ("NEGATIVO", "Negativo"),
        ("NEUTRO", "Neutro"),
    ]

    texto = models.CharField(max_length=100, null=False, blank=False)
    resposta = models.TextField(null=False, blank=False)
    data_e_hora = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    categoria = models.CharField(max_length=100, default='', choices=OPCOES_CATEGORIA)
    publicada = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to="imagens/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.texto

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username