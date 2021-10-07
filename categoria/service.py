from .models import Categoria


class CategoriaService():
    def buscar_todas_categorias(self):
        return Categoria.objects.all()    

    def buscar_categoria_by_id(self, id:int) -> Categoria:
        return Categoria.objects.filter(id=id).first()