from visao.sistemavisao import SistemaVisao
from controlador.filmecontrolador import FilmeControlador
from controlador.salacontrolador import SalaControlador
from controlador.sessaocontrolador import SessaoControlador


class SistemaControlador:

    def __init__(self):
        self.__filmecontrolador = FilmeControlador(self)
        self.__salacontrolador = SalaControlador(self)
        self.__sessaocontrolador = SessaoControlador(self)
        self.__sistemavisao = SistemaVisao()

    @property
    def filmecontrolador(self):
        return self.__filmecontrolador

    @property
    def salacontrolador(self):
        return self.__salacontrolador

    @property
    def sessaocontrolador(self):
        return self.__sessaocontrolador

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_filme(self):
        self.__filmecontrolador.abre_tela()

    def cadastra_sessao(self):
        # Chama o controlador de Amigos
        self.__sessaocontrolador.abre_tela()

    def cadastra_sala(self):
        self.__salacontrolador.abre_tela()
        # Chama o controlador de Emprestimos

    def encerra_sistema(self):
        exit(0)

    def relatorio_sessoes(self):
        self.__sessaocontrolador.relatorio_sessoes()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_sala, 2: self.cadastra_filme, 3: self.cadastra_sessao,
                        4: self.relatorio_sessoes,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__sistemavisao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
