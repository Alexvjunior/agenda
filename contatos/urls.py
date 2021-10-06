from django.urls import path
from .views import ContatosView, ContatosBuscaView, ContatosAdicionarView, ContatosEditarView

urlpatterns = [
    path('', ContatosView.as_view(), name='home'),
    path('<int:contato_id>', ContatosView.as_view(), name='ver_contato'),
    path('busca/', ContatosBuscaView.as_view(), name='busca'),
    path('adicionar', ContatosAdicionarView.as_view(), name='adicionar'),
    path('editar/<int:contato_id>', ContatosEditarView.as_view(), name='editar'),
]