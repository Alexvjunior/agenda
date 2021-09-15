from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

class ContatosView(APIView):
    def get(self, request):
        return render(request, 'home.html')