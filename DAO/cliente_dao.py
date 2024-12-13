from abstrato.dao import DAO
from entidade.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self, datasource='clientes.pkl'):
        super().__init__(datasource)

    def add(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            super().add(cliente.cpf, cliente)

    def update(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            super().update(cliente.cpf, cliente)

    def get_all(self):
        """Retorna todos os clientes."""
        return super().get_all()

    def get_by_cpf(self, cpf: str):
        """Busca um cliente pelo CPF."""
        return super().get(cpf)
