#Sala
#Atributos: número, capacidade, tipo (2D, 3D, IMAX).
#Métodos: adicionarSala(), atualizarSala(), removerSala().


class Sala:

    salas_db = []

    def __init__(self, numero: int, capacidadnt: int, tipo: str): #Fazer o isIntance do tipos de dados
        self.__numero = numero
        self.__capacidade = capacidade
        self.__tipo = tipo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    def adicionarSala(self):
        """
        Aqui iremos adicionar a sala a uma lista de salas para podermos utilizar essa lista posteriormente.
        Retorna uma confirmação: "sala(número da sala) foi adicionado com sucesso!"
        """

    def atualizarSala(self, numero=None, capacidade=None, tipo=None):
        """
         Método para atualizar os atributos da sala, caso as informações sejam passadas corretamente (não forem Null).
         Retorna os novos atributos.
         """

    def removerSala(self):
        """
           Método para remover uma sala do sistema, caso a sala que queremos excluir esteja cadastrada.
           Retorna a confirmação com o número da sala exluída caso ela exista.
           Retorna "Sala (número da sala) não encontrado" caso a sala fornecida não esteja na lista de salas.
           """
