from datetime import time

class Filme:    
    def __init__(self, titulo: str, duracao: int, classificacao_etaria: int):
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao_etaria = classificacao_etaria

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
    def duracao(self, duracao: int):
        if not isinstance(duracao, int):
            raise ValueError("Duração inválida. Valor de tempo deve estar em minutos.")
        self.__duracao = duracao

    @property
    def classificacao_etaria(self):
        return self.__classificacao_etaria

    @classificacao_etaria.setter
    def classificacao_etaria(self, classificacao_etaria: int):
        self.__classificacao_etaria = classificacao_etaria
