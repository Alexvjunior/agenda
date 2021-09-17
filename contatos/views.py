from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from . import service

class ContatosView(APIView):
    def get(self, request, contato_id=None):
        if contato_id is None:
            contatos = service.buscar_todos_contatos()
            return render(request=request, template_name='home.html', context={'contatos': contatos})
        
        contato = service.buscar_contato_por_id(contato_id)
        return render(request=request, template_name='contato.html', context={'contato': contato})
