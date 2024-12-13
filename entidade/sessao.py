from entidade.filme import Filme
from entidade.sala import Sala
from enum import Enum

class Sessao:
    #TODO opcao 1: criar uma chave unica com random, gerando um numero grande e passando com um atributo.
    #TODO opcao 2: criar um singleton(slides), e incrementar um contador.
    sessoes_db = []

    def __init__(self, filme: Filme, sala: Sala, horario: str, codigo: int, tipo: str):
        if isinstance(filme, Filme):
            self.__filme = filme
        if isinstance(sala, Sala):
            self.__sala = sala
        if isinstance(horario, str):
            self.__horario = horario
        if isinstance(codigo, int):
            self.__codigo = codigo
        self.tipo = tipo
        self.__ingressos = []

    @property
    def filme(self) -> Filme:
        return self.__filme

    @filme.setter
    def filme(self, filme: filme):
        if isinstance(filme, Filme):
            self.__filme = filme

    @property
    def sala(self) -> Sala:
        return self.__sala

    @sala.setter
    def sala(self, sala: Sala):
        if isinstance(sala, Sala):
            self.__sala = sala

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario: str):
        self.__horario = horario

    @property
    def ingressos_disponiveis(self) -> int:
        return self.__sala.capacidade - len(self.__ingressos)

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    def adicionar_ingresso(self, ingresso):
         self.__ingressos.append(ingresso)
