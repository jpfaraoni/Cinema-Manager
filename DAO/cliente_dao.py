from abstrato.dao import DAO
from entidade.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        super().add(cliente.nome, cliente)
        super().add(cliente.email, cliente)
        super().add(cliente.idade, cliente)
        super().add(cliente.telefone, cliente)

    def update(self, cliente: Cliente):
        if cliente and isinstance(cliente, Cliente):
            super().update(cliente.nome, cliente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)

