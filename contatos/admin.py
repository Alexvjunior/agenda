from django.contrib import admin
from .models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobre_nome', 'email', 'data_criacao', 'categoria')
    list_display_links = ('id', 'nome')
    list_filter = ('categoria',)
admin.site.register(Contato, ContatoAdmin)