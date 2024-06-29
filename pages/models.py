from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/')
    descricao = models.TextField(max_length=600)

    def __str__(self):
        return self.nome