from sistema_visao import SistemaVisao
from controlador.filme_controlador import FilmeControlador
from controlador.sala_controlador import SalaControlador
from controlador.sessao_controlador import SessaoControlador

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
        # Chama o controlador de Sessão
        self.__sessaocontrolador.abre_tela()

    def cadastra_sala(self):
        self.__salacontrolador.abre_tela()

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
            funcao_escolhida = lista_opcoes.get(opcao_escolhida)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                print("Opção inválida. Tente novamente.")
