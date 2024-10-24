# Sessão
# Atributos: filme, sala, horário, data, ingressosDisponíveis.
# Métodos: criarSessão(), atualizarSessão(), cancelarSessão().

from filme import Filme
from sala import Sala
from datetime import time


class SessaoModelo:
    sessoes_db = []

    def __init__(self, filme: Filme, sala: Sala, horario: time):
        self.__filme = filme
        self.__sala = sala
        self.__horario = time

    @property
    def filme(self) -> Filme:
        return self.__filme

    @filme.setter
    def filme(self, filme: filme):
        self.__filme = filme

    @property
    def sala(self) -> Sala:
        return self.__sala

    @sala.setter
    def sala(self, sala: Sala):
        self.__sala = sala

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario: str):
        self.__horario = horario

    # def __str__(self):
    #     return (f"Filme: {self.__filme}\n"
    #             f"Sala: {self.__sala}\n"
    #             f"Horário: {self.__horario}\n"
    #             f"ingressos_disponiveis: {self.__ingressos_disponiveis}\n")

    #TODO transformar essa funcao em uma matriz com os filmes organizados por horario.
    def infoSessoes(self):
        for sessao in sessoes_db:
            print(
                f"Filme: {sessao.filme.titulo}, Sala: {sessao.sala.tipo}, Horário: {sessao.horario}, Ingressos disponíveis: {sessao.ingressos_disponiveis}")
