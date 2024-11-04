class Filme:
    def __init__(self, titulo: str, duracao: int, genero: str, classificacao_etaria: int):
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao_etaria = classificacao_etaria
        self.genero = genero

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
        # if not duracao or not isinstance(duracao, str):
        #     raise ValueError("Duração inválida.")
        self.__duracao = duracao

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        # if not duracao or not isinstance(duracao, str):
        #     raise ValueError("Duração inválida.")
        self.__genero = genero
    # @property
    # def genero(self):
    #     return self.__genero
    #
    # @genero.setter
    # def genero(self, genero: str):
    #     if not genero or not isinstance(genero, str):
    #         raise ValueError("Gênero inválido.")
    #     self.__genero = genero

    @property
    def classificacao_etaria(self):
        return self.__classificacao_etaria

    @classificacao_etaria.setter
    def classificacao_etaria(self, classificacao_etaria: int):
        if not isinstance(classificacao_etaria, int) or classificacao_etaria < 0:
            raise ValueError("Classificação etária inválida.")
        self.__classificacao_etaria = classificacao_etaria

    # @property
    # def sinopse(self):
    #     return self.__sinopse
    #
    # @sinopse.setter
    # def sinopse(self, sinopse: str):
    #     if not sinopse or not isinstance(sinopse, str):
    #         raise ValueError("Sinopse inválida.")
    #     self.__sinopse = sinopse
