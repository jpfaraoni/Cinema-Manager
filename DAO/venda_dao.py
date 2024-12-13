from abstrato.dao import DAO
from entidade.venda import Venda

class VendaDAO(DAO):
    def __init__(self):
        super().__init__('vendas.pkl')

    def add(self, venda: Venda):
        if isinstance(venda, Venda):
            super().add(venda.ingresso.id, venda)

    def update(self, venda: Venda):
        if isinstance(venda, Venda):
            super().update(venda.ingresso.id, venda)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
