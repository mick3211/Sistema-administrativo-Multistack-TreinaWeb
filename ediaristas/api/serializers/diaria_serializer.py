from rest_framework.serializers import ModelSerializer, DecimalField, ValidationError
from ..models import Diaria, Usuario
from administracao.services.servico_service import listar_servico_id
from ..services.cidades_atendimento_service import verificar_disponibilidade_cidade, buscar_cidade_ibge


class UsuarioDiariaSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'nascimento', 'telefone', 'tipo_usuario', 'reputacao', 'foto_usuario')


class DiariaSerializer(ModelSerializer):
    cliente = UsuarioDiariaSerializer(read_only=True)
    valor_comissao = DecimalField(read_only=True, max_digits=5, decimal_places=2)
    class Meta:
        models = Diaria
        fields = '__all__'

    
    def validate(self, attrs):
        if not verificar_disponibilidade_cidade(attrs['cep']):
            raise ValidationError('Não há diaristas para o CEP informado')
        return attrs

    def validate_codigo_ibge(self, codigo_ibge):
        buscar_cidade_ibge(codigo_ibge)
        return codigo_ibge

    def validate_preco(self, preco):
        servico = listar_servico_id(self.initial_data['servico'].id)
        if servico is None:
            raise ValidationError('Servico não existe')
        valor_total = 0
        valor_total += servico.valor_quarto * self.initial_data['quantidade_quartos']
        valor_total += servico.valor_sala * self.initial_data['quantidade_salas']
        valor_total += servico.valor_banheiro * self.initial_data['quantidade_banheiros']
        valor_total += servico.valor_cozinha * self.initial_data['quantidade_cozinhas']
        valor_total += servico.valor_quintal * self.initial_data['quantidade_quintais']
        valor_total += servico.valor_outros * self.initial_data['quantidade_outros']
        if preco >= servico.valor_minimo:
            if valor_total < servico.valor_minimo:
                return servico.valor_minimo
            if preco == valor_total:
                return preco
            raise ValidationError('Valor não corresponde ao serviço contratado')
        raise ValidationError('Valor abaixo do valor mínimo do serviço')
    
    def validate_tempo_atendimento(self, tempo_atendimento):
        servico = listar_servico_id(self.initial_data['servico'].id)
        if servico is None:
            raise ValidationError('Servico não existe')
        horas_total = 0
        horas_total += servico.horas_quarto * self.initial_data['horas_quartos']
        horas_total += servico.horas_sala * self.initial_data['horas_salas']
        horas_total += servico.horas_banheiro * self.initial_data['horas_banheiros']
        horas_total += servico.horas_cozinha * self.initial_data['horas_cozinhas']
        horas_total += servico.horas_quintal * self.initial_data['horas_quintais']
        horas_total += servico.horas_outros * self.initial_data['horas_outros']
        if tempo_atendimento != horas_total:
            raise ValidationError('Valores não correspondem')
        return tempo_atendimento

    def validate_data_atendimento(self, data_atendimento):
        if data_atendimento.hour < 6:
            raise ValidationError('Horário de início não pode ser menor que 06:00')
        if (data_atendimento.hour + self.initial_data['tempo_atendimento']) > 22:
            raise ValidationError('Horário de atendimento não pode passar das 22:00')
        return data_atendimento
    
    def create(self, validated_data):
        servico = listar_servico_id(validated_data['servico'].id)
        valor_comissao = validated_data['preco'] * servico.porcentagem_comissao / 100
        client_id = self.context['request'].user.id
        diaria = Diaria.objects.create(client_id=client_id, valor_comissao=valor_comissao, **validated_data)
        return diaria
