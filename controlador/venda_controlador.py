from entidade.venda import Venda
from entidade.cliente import Cliente
from exception.ingresso_indisponivel import IngressoIndisponivel
from exception.idade_invalida import IdadeInvalida
from visao.venda_visao import VendaVisao
from datetime import datetime
from abstrato.controlador_entidade_abstrata import ControladorEntidadeAbstrata

class VendaControlador(ControladorEntidadeAbstrata):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__controlador_sistema = controlador_sistema
        self.__vendas = []  # Lista de vendas realizadas
        self.__vendavisao = VendaVisao()

    def registrar_venda(self):
        try:
            self.__controlador_sistema.__sessaocontrolador.listar_sessoes()
            self.__controlador_sistema.__clientecontrolador.listar_clientes()

            dados_venda = self.__vendavisao.pega_dados_venda()

            sessao = self.__controlador_sistema.__sessaocontrolador.busca_sessao(
                dados_venda["titulo"], dados_venda["sala_numero"], dados_venda["horario"]
            )
            cliente = self.__controlador_sistema.__clientecontrolador.busca_cliente(dados_venda["cpf_cliente"])

            if cliente.idade < sessao.filme.classificacao_etaria:
                raise IdadeInvalida(cliente.idade, sessao.filme.classificacao_etaria)

            if not sessao.ingressos_disponiveis():
                raise IngressoIndisponivel(sessao)

            venda = Venda(sessao, cliente, dados_venda["metodo_pagamento"], datetime.now())
            self.__vendas.append(venda)

            sessao.vender_ingresso()
            self.__vendavisao.mostra_mensagem(f"Venda realizada com sucesso para {cliente.nome}!")
        except IdadeInvalida as e:
            self.__vendavisao.mostra_mensagem(f"Erro: {e}")
        except IngressoIndisponivel as e:
            self.__vendavisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__vendavisao.mostra_mensagem(f"Erro inesperado: {e}")

    def listar_vendas(self):
        if not self.__vendas:
            self.__vendavisao.mostra_mensagem("Nenhuma venda realizada.")
        else:
            for venda in self.__vendas:
                self.__vendavisao.mostra_venda({
                    "cliente_nome": venda.cliente.nome,
                    "filme": venda.sessao.filme.titulo,
                    "sala": venda.sessao.sala.numero,
                    "horario_sessao": venda.sessao.horario,
                    "horario_compra": venda.horario_compra.strftime("%Y-%m-%d %H:%M"),
                    "metodo_pagamento": venda.metodo_pagamento
                })

    def gerar_relatorio_vendas(self):
        total_vendas_por_filme = {}
        for venda in self.__vendas:
            filme = venda.sessao.filme.titulo
            if filme in total_vendas_por_filme:
                total_vendas_por_filme[filme] += 1
            else:
                total_vendas_por_filme[filme] = 1

        self.__vendavisao.mostra_relatorio_vendas(total_vendas_por_filme)

    def atualizar_venda(self):
        try:
            self.listar_vendas()
            indice_venda = self.__vendavisao.seleciona_venda(self.__vendas)

            if indice_venda is not None:
                venda = self.__vendas[indice_venda]
                if datetime.now() > venda.sessao.horario:
                    self.__vendavisao.mostra_mensagem("Venda não pode ser atualizada após o início da sessão.")
                    return

                novo_metodo_pagamento = self.__vendavisao.pega_metodo_pagamento()
                venda.metodo_pagamento = novo_metodo_pagamento
                self.__vendavisao.mostra_mensagem(f"Método de pagamento atualizado para {venda.cliente.nome}.")
            else:
                self.__vendavisao.mostra_mensagem("Nenhuma venda selecionada.")
        except Exception as e:
            self.__vendavisao.mostra_mensagem(f"Erro ao atualizar venda: {e}")

    def cancelar_venda(self):
        try:
            self.listar_vendas()
            indice_venda = self.__vendavisao.seleciona_venda(self.__vendas)

            if indice_venda is not None:
                venda = self.__vendas[indice_venda]
                if datetime.now() > venda.sessao.horario:
                    self.__vendavisao.mostra_mensagem("Venda não pode ser cancelada após o início da sessão.")
                    return

                venda.sessao.cancelar_ingresso_vendido()
                self.__vendas.pop(indice_venda)
                self.__vendavisao.mostra_mensagem(f"Venda cancelada para {venda.cliente.nome}.")
            else:
                self.__vendavisao.mostra_mensagem("Nenhuma venda selecionada.")
        except Exception as e:
            self.__vendavisao.mostra_mensagem(f"Erro ao cancelar venda: {e}")

    def abre_tela(self):
        lista_opcoes = {1: self.registrar_venda, 2: self.atualizar_venda, 3: self.cancelar_venda, 
                        4: self.listar_vendas, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__vendavisao.tela_opcoes()]()
