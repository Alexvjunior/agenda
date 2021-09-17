from .models import Contato

def buscar_todos_contatos():
    return Contato.objects.all()

def buscar_contato_por_id(id:int) -> Contato:
    return Contato.objects.filter(id=id).first()