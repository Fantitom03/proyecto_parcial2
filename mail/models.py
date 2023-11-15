from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    pass


class Mail(models.Model):
    usuario_origen = models.ForeignKey(User, on_delete=models.CASCADE)
    mail_origen = models.EmailField(max_length=254)
    destinatario = models.EmailField(max_length=254)
    asunto = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    pass
