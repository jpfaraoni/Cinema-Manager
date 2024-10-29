from enum import Enum

class MetodoDePagamento(Enum):
    DINHEIRO = "dinheiro"
    CARTAO_CREDITO = "cartão de crédito"
    CARTAO_DEBITO = "cartão de débito"
