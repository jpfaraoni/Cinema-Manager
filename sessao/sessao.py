# Sessão
# Atributos: filme, sala, horário, data, ingressosDisponíveis.
# Métodos: criarSessão(), atualizarSessão(), cancelarSessão().

from filme import Filme
from sala import Sala
from enum import Enum

class TipoSessao(Enum):
    _2D = 1
    _3D = 2
    _IMAX = 3


class Sessao:
    sessoes_db = []

    def __init__(self, filme: Filme, sala: Sala, horario: str, capacidade_maxima: int, tipo= TipoSessao):
        if isinstance(filme, Filme):
            self.__filme = filme
        if isinstance(sala, Sala):
            self.__sala = sala
        if isinstance(horario, str):
            self.__horario = horario
        if isinstance(capacidade_maxima, int):
            self.__capacidade_maxima = capacidade_maxima
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
    def capacidade_maxima(self) -> int:
        return self.__capacidade_maxima

    @capacidade_maxima.setter
    def capacidade_maxima(self, capacidade_maxima):
        self.__capacidade_maxima = capacidade_maxima

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    def adicionar_ingresso(self, ingresso):
         self.__ingressos.append(ingresso)  # Método para adicionar um ingresso

