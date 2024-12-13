from abstrato.dao import DAO
from entidade.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self, datasource='clientes.pkl'):
        # O datasource é passado como parâmetro para o arquivo de persistência
        super().__init__(datasource)

    def add(self, cliente: Cliente):
        """Adiciona um cliente ao cache e salva no arquivo."""
        if isinstance(cliente, Cliente):
            super().add(cliente.cpf, cliente)

    def remove(self, cpf: str):
        """Remove um cliente pelo CPF do cache e salva no arquivo."""
        super().remove(cpf)

    def update(self, cliente: Cliente):
        """Atualiza um cliente no cache e salva no arquivo."""
        if isinstance(cliente, Cliente):
            super().update(cliente.cpf, cliente)

    def get_all(self):
        """Retorna todos os clientes."""
        return super().get_all()

    def get_by_cpf(self, cpf: str):
        """Busca um cliente pelo CPF."""
        return super().get(cpf)
