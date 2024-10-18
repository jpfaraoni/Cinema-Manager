class Filme:    
    def __init__(self, titulo: str, duracao: str, genero: str, classificacao_etaria: int, sinopse: str):
        self.__titulo = titulo
        self.__duracao = duracao
        self.__genero = genero
        self.__classificacao_etaria = classificacao_etaria
        self.__sinopse = sinopse

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: str):
        self.__duracao = duracao

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero

    @property
    def classificacao_etaria(self):
        return self.__classificacao_etaria

    @classificacao_etaria.setter
    def classificacao_etaria(self, classificacao_etaria: int):
        self.__classificacao_etaria = classificacao_etaria

    @property
    def sinopse(self):
        return self.__sinopse

    @sinopse.setter
    def sinopse(self, sinopse: str):
        self.__sinopse = sinopse
