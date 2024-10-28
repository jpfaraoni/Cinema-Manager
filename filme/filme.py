from datetime import time
from enum import Enum

class ClassificacaoEtaria(Enum):
    LIVRE = 0
    DEZ = 10
    DOZE = 12
    CATORZE = 14
    DEZESSEIS = 16
    DEZOITO = 18

class Filme:    
    def __init__(self, titulo: str, duracao: time, genero: str, classificacao_etaria: ClassificacaoEtaria, sinopse: str):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero
        self.classificacao_etaria = classificacao_etaria
        self.sinopse = sinopse

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if not titulo or not isinstance(titulo, str):
            raise ValueError("Título inválido.")
        self.__titulo = titulo

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: time):
        if not isinstance(duracao, time):
            raise ValueError("Duração inválida. Use um objeto do tipo datetime.time.")
        self.__duracao = duracao

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        if not genero or not isinstance(genero, str):
            raise ValueError("Gênero inválido.")
        self.__genero = genero

    @property
    def classificacao_etaria(self):
        return self.__classificacao_etaria

    @classificacao_etaria.setter
    def classificacao_etaria(self, classificacao_etaria: ClassificacaoEtaria):
        if not isinstance(classificacao_etaria, ClassificacaoEtaria):
            raise ValueError("Classificação etária inválida.")
        self.__classificacao_etaria = classificacao_etaria

    @property
    def sinopse(self):
        return self.__sinopse

    @sinopse.setter
    def sinopse(self, sinopse: str):
        if not sinopse or not isinstance(sinopse, str):
            raise ValueError("Sinopse inválida.")
        self.__sinopse = sinopse
