from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.utils import timezone
from categoria.models import Categoria

class Contato(models.Model):

    nome = models.CharField(max_length=30)
    sobre_nome = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    telefone = models.CharField(max_length=20, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(to=Categoria, on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return self.nome