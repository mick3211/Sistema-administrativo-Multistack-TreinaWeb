from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..hateoas import Hateoas
from django.urls import reverse

class Inicio(APIView):
    def get(self, request, format=None):
        links = Hateoas()
        links.add_get('listar_srvicos', reverse('servico-list'))
        links.add_get('endereco_cep', reverse('endereco-cep-list'))
        links.add_get('diaristas_localidade', reverse('diaristas-localidades-list'))
        links.add_get('verificar_disponibilidade_atendimento', reverse('disponibilidade-atendimento-cidade'))

        return Response({'links': links.to_array()}, status=status_http.HTTP_200_OK)