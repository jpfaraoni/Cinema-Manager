from clientemodelo import ClienteModelo

class ClienteControlador:

  """
    Classe que controla as operações sobre o modelo Cliente.

    Atributos:
    - clientes_db: Lista que simula um banco de dados em memória para os clientes.
    """

    clientes_db = []  # Simulação do banco de dados em memória
def cadastrarCliente(self):
        #Cadastra o cliente
        Cliente.clientes_db.append(self)
        return f"Cliente: '{self.__nome}' adicionado com sucesso."

    def atualizarCliente(self, nome=None, fone=None, email=None):
        # Atualiza os atributos do cliente se os novos valores forem fornecidos
        if nome is not None:
            self.__nome = nome
        if fone is not None:
            self.__fone = fone
        if email is not None:
            self.__email = email
        return f"Cliente atualizado: {self.__nome}, {self.__fone}, {self.__email}"

    def removerCliente(self):
        # Remove o cliente do "banco de dados"
        if self in Cliente.clientes_db:
            Cliente.clientes_db.remove(self)
            return f"Cliente '{self.__nome}' removido com sucesso."
        else:
            return f"Cliente '{self.__nome}' não encontrado."

    def __str__(self):
        return (f"Nome: {self.__nome}\n"
                f"Fone: {self.__fone}\n"
                f"Email: {self.__email}\n")
      
    def listar_clientes(self):
        """
        Retorna a lista de clientes cadastrados.
        Se a lista estiver vazia, retorna uma mensagem de aviso.
        """
        if not ClienteControlador.clientes_db:
            return "Nenhum cliente cadastrado."

        return ClienteControlador.clientes_db  # Retorna a lista de objetos ClienteModelo
