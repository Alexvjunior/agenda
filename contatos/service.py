from categoria.models import Categoria
from categoria.service import CategoriaService
import contatos
from .models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat

_SERVICE_CATEGORIA = CategoriaService()

def buscar_todos_contatos():
    return Contato.objects.all().filter(
        ativo=True
    )

def buscar_contato_por_id(id:int) -> Contato:
    return Contato.objects.filter(id=id).first()

def buscar_contatos_by_termo(termo:str):
    campos = Concat('nome', Value(' '), 'sobre_nome')

    return Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo) | Q(email__icontains=termo),
        ativo=True,
    ).order_by('nome')

def deletar_contato_by_id(id:int) -> int:
    return Contato.objects.filter(id=id).delete()

def editar_contato_by_id(id:int, data:dict):
    return Contato.objects.filter(id=id).update(**data)


def editar_contato(contato:Contato, data:dict, categoria:Categoria) -> None:
    contato.nome = data['nome']
    contato.sobre_nome = data['sobre_nome']
    contato.telefone = data['telefone']
    contato.email = data['email']
    contato.categoria = categoria
    contato.save()