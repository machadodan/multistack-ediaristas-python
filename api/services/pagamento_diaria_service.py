from ..models import Pagamento
from .diaria_service import atualizar_staus_diaria

def realizar_pagamento(diaria, card_hash):
    Pagamento.objects.create(status="pago",
    valor=diaria.preco, transacao_id="12a9daqwe",
    diaria=diaria)
    atualizar_staus_diaria(diaria.id,2 )
    return 
