class Ingresso:
    def __init__(self, sessao: Sessao, cliente: Cliente):
        if isinstance(sessao, Sessao):
            self.__sessao = sessao
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def sessao(self) -> Sessao:
        return self.__sessao

    @sala.setter
    def sessao(self, sessao: Sessao):
        if isinstance(sessao, Sessao):
            self.__sessao = sessao

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @filme.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
