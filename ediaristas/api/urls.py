from django.urls import path
from .views import (diaristas_localidade_view,
                    endereco_cep_view,
                    disponibilidade_atendimento_cidade_view,
                    servico_view,
                    inicio_view,
                    usuario_view,
                    me_view,
                    diaria_view,
                    pagamento_diaria_view
                    )

urlpatterns = [
    path('', inicio_view.Inicio.as_view(), name='inicio'),
    path('diaristas/localidades', diaristas_localidade_view.DiaristasLocalidades.as_view(), name='diaristas-localidades-list'),
    path('diaristas/disponibilidade', disponibilidade_atendimento_cidade_view.DisponibilidadeAtendimentoCidade.as_view(), name='disponibilidade-atendimento-cidade'),
    path('enderecos', endereco_cep_view.EnderecoCep.as_view(), name='endereco-cep-list'),
    path('servicos', servico_view.Servico.as_view(), name='servico-list'),
    path('usuarios', usuario_view.Usuario.as_view(), name='usuario-list'),
    path('me', me_view.Me.as_view(), name='me-list'),
    path('diarias', diaria_view.DiariaView.as_view(), name='diaria-list'),
    path('diarias/<int:diaria_id>', diaria_view.DiariaId.as_view(), name='diaria-detail'),
    path('diarias/<int:diaria_id>/pagamentos', pagamento_diaria_view.PagamentoDiaria.as_view(), name='pagamento-diaria-list'),
]