from django.urls import path
from .views import (diaristas_localidade_view,
                    endereco_cep_view,
                    disponibilidade_atendimento_cidade_view,
                    servico_view,
                    inicio_view,
                    )

urlpatterns = [
    path('diaristas/localidades', diaristas_localidade_view.DiaristasLocalidades.as_view(), name='diaristas-localidades-list'),
    path('diaristas/disponibilidade', disponibilidade_atendimento_cidade_view.DisponibilidadeAtendimentoCidade.as_view(), name='disponibilidade-atendimento-cidade'),
    path('enderecos', endereco_cep_view.EnderecoCep.as_view(), name='endereco-cep-list'),
    path('servicos', servico_view.Servico.as_view(), name='servico-list'),
    path('', inicio_view.Inicio.as_view(), name='inicio'),
]