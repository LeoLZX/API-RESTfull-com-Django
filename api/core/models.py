from django.db import models

class Produtos(models.Model):
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=50)
    preco = models.IntegerField()

    def __str__(self):
        return self.descricao
