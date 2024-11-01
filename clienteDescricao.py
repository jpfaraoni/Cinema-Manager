#Cliente
#Atributos: nome, email, telefone, históricoDeCompras.
#Métodos: cadastrarCliente(), atualizarCliente(), removerCliente().

class Cliente:
    clientes_db = []
"""
A classe Cliente tem como objetivo guardar e fazer operações com os dados do cliente.
Atributos:
- nome
- email
- telefone
- históricoDeCompras (lista com o histórico de compras do cliente)
"""
    clientes_db = [] #lista em que armazenaremos todos os clientes.

    def __init__(self, nome: str, email: str, telefone: str):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade

   @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone: str):
        self.__fone = fone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

def cadastrar_cliente(self):
    """
    Aqui, iremos adicionar lógica para armazenar o cliente em uma lista.
    """
    pass


def atualizar_cliente(self):
    """
    Método para atualizar os atributos do cliente, caso as informações sejam passadas (não forem Null).
    Retorna o cliente atualizado.
    """
    pass


def remover_cliente(self):
    """
    Método para remover um cliente do sistema, caso o cliente que queremos excluir esteja cadastrado.
    Retorna a confirmação com o nome do cliente exluído caso ele exista.
    Retorna "Cliente (nome do cliente) não encontrado" caso o nome fornecido não pertença a um cliente.
    """
    pass

