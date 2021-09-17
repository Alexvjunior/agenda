from django.urls import path
from .views import ContatosView

urlpatterns = [
    path('', ContatosView.as_view(), name='home'),
    path('<int:contato_id>', ContatosView.as_view(), name='ver_contato'),
]