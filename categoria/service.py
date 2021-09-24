from .models import Categoria


class CategoriaService():
    def buscar_todas_categorias(self):
        return Categoria.objects.all()    