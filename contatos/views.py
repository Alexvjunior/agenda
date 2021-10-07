from django.shortcuts import render
from rest_framework.views import APIView
from . import service
from django.core.paginator import Paginator
from .serializers import ContatosSerializer
from categoria.service import CategoriaService
from django.http import HttpResponseRedirect


CATEGORIA_SERVICE = CategoriaService()

class ContatosView(APIView):
    def get(self, request, contato_id=None):
        if contato_id is None:
            contatos = service.buscar_todos_contatos()
            paginator = Paginator(contatos, 3)
            page = request.GET.get('p')
            contatos = paginator.get_page(page)
            return render(request=request, template_name='home.html', context={'contatos': contatos})
        
        contato = service.buscar_contato_por_id(contato_id)
        return render(request=request, template_name='contato.html', context={'contato': contato})

    def post(self, request, contato_id):
        service.deletar_contato_by_id(contato_id)
        return HttpResponseRedirect('/')

class ContatosBuscaView(APIView):
    def get(self, request):
        termo = request.GET.get('termo')
        contatos = service.buscar_contatos_by_termo(termo)
        paginator = Paginator(contatos, 3)
        page = request.GET.get('p')
        contatos = paginator.get_page(page)
        return render(request=request, template_name='home.html', context={'contatos': contatos})

class ContatosAdicionarView(APIView):
    def get(self, request):
        categorias = CATEGORIA_SERVICE.buscar_todas_categorias()
        return render(request=request, template_name='adicionar.html', context={"categorias":categorias})

    def post(self, request, contato_id=None):
        serializer = ContatosSerializer(data=request.data)
        if not serializer.is_valid():
            categorias = CATEGORIA_SERVICE.buscar_todas_categorias()
            return render(request=request, template_name='adicionar.html', context={"valido":False, "mensagem":"Verifique os campos e tente novamente", "categorias":categorias})
        if contato_id is None:
            serializer.save()
        else:
            service.editar_contato_by_id(contato_id, serializer.data)
        return HttpResponseRedirect('/')

class ContatosEditarView(APIView):

    def get(self, request, contato_id):
        contato = service.buscar_contato_por_id(contato_id)
        categorias = CATEGORIA_SERVICE.buscar_todas_categorias()
        return render(request=request, template_name='editar.html', context={"categorias":categorias, "contato":contato})


    def post(self, request, contato_id=None):
        if contato_id is not None:
            contato = service.buscar_contato_por_id(contato_id)
            categorias = CATEGORIA_SERVICE.buscar_todas_categorias()
            return render(request=request, template_name='editar.html', context={"categorias":categorias, "contato":contato})
        serializer = ContatosSerializer(data=request.data)
        if not serializer.is_valid():
            categorias = CATEGORIA_SERVICE.buscar_todas_categorias()
            return render(request=request, template_name='editar.html', context={"valido":False, "mensagem":"Verifique os campos e tente novamente", "categorias":categorias})
        contato = service.buscar_contato_por_id(id)
        categoria = CATEGORIA_SERVICE.buscar_categoria_by_id( request.data.get('categoria'))
        service.editar_contato(contato, request.data, categoria)
        return HttpResponseRedirect('/')