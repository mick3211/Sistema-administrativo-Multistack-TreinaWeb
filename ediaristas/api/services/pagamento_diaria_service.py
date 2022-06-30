from ..models import Pagamento
from .diaria_service import atualizar_status_diaria


def realizar_pagamento(diaria, card_hash):
    Pagamento.objects.create(status='pago', valor=diaria.preco,
        transacao_id='dasd123451sda', diaria=diaria)
    atualizar_status_diaria(diaria.id, 2)
    return