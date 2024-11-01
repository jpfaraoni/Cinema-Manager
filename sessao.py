
from filme import Filme
from sala import Sala
<<<<<<< HEAD
=======
from enum import Enum

class TipoSessao(Enum):
    _2D = 1
    _3D = 2
    _IMAX = 3

>>>>>>> 749178d8ec62e7324d97a220842dd5b11bc18c75

class Sessao:
    sessoes_db = []

<<<<<<< HEAD
    def __init__(self, filme: Filme, sala: Sala, horario: str, capacidade_maxima: int, tipo= str):
=======
    def __init__(self, filme: Filme, sala: Sala, horario: str, tipo= TipoSessao):
>>>>>>> 749178d8ec62e7324d97a220842dd5b11bc18c75
        if isinstance(filme, Filme):
            self.__filme = filme
        if isinstance(sala, Sala):
            self.__sala = sala
        if isinstance(horario, str):
            self.__horario = horario
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
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    def adicionar_ingresso(self, ingresso):
        if ingresso is not None:
            self.__ingressos.append(ingresso)  # Método para adicionar um ingresso

    def ingressos_disponiveis(self) -> int:
        return self.sala.capacidade - len(self.__ingressos)

