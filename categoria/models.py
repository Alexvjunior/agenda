from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        db_table = 'CATEGORIA'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
