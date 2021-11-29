from django.urls import path
from .views import cadastrar_servico, editar_servico, listar_servicos

urlpatterns = [
    path('servicos/cadastrar', cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar', listar_servicos, name='listar_servicos'),
    path('servicos/editar/<int:id>', editar_servico, name='editar_servico'),
]