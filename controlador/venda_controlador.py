from entidade.venda import Venda
from entidade.cliente import Cliente
from entidade.ingresso import Ingresso
from exception.ingresso_indisponivel import IngressoIndisponivel
from exception.idade_invalida import IdadeInvalida
from visao.venda_visao import VendaVisao
from DAO.venda_dao import VendaDAO
from datetime import datetime
from abstrato.controlador_entidade_abstrata import ControladorEntidadeAbstrata
from controlador.sessao_controlador import SessaoControlador
from controlador.cliente_controlador import ClienteControlador
from exception.cliente_nao_encontrado import ClienteNaoEncontrado

class VendaControlador(ControladorEntidadeAbstrata):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__controlador_sistema = controlador_sistema
        self.__venda_DAO = VendaDAO()
        self.__vendavisao = VendaVisao()
        self.__clientecontrolador = ClienteControlador(self)  # Controlador de Cliente
        self.__sessaocontrolador = SessaoControlador(self)  # Controlador de Sessão

    def registrar_venda(self):
        try:
            # Exibir todas as sessões disponíveis
            self.__sessaocontrolador.listar_sessoes()

            # Solicitar o código da sessão ao usuário
            codigo_sessao = self.__vendavisao.pega_codigo_sessao()
            if codigo_sessao is None:
                return

            # Buscar a sessão pelo código
            sessao = self.__sessaocontrolador.busca_sessao(codigo=codigo_sessao)

            # Listar clientes para o usuário
            self.__clientecontrolador.lista_clientes()
            cpf_cliente = self.__vendavisao.pega_cpf_cliente()
            
            # Verificar se o CPF é válido e buscar o cliente
            try:
                cliente = self.__clientecontrolador.busca_cliente_por_cpf(cpf_cliente)  # Usar busca por CPF
            except ClienteNaoEncontrado:
                self.__vendavisao.mostra_mensagem("Cliente não encontrado com esse CPF.")
                return

            # Validar a idade do cliente
            if cliente.idade < sessao.filme.classificacao_etaria:
                raise IdadeInvalida(cliente.idade, sessao.filme.classificacao_etaria)

            # Verificar disponibilidade de ingressos
            if sessao.ingressos_disponiveis <= 0:
                raise IngressoIndisponivel(sessao)

            # Criar o ingresso e registrar a venda
            ingresso = Ingresso(cliente, sessao)
            metodo_pagamento = self.__vendavisao.pega_metodo_pagamento()
            venda = Venda(ingresso, datetime.now(), metodo_pagamento)
            self.__venda_DAO.add(venda)

            # Atualizar a quantidade de ingressos disponíveis
            sessao.ingressos_disponiveis -= 1

            # Confirmar o sucesso da venda
            self.__vendavisao.mostra_mensagem(f"Venda realizada com sucesso para {cliente.nome}!")
        except IdadeInvalida as e:
            self.__vendavisao.mostra_mensagem(f"Erro: {e}")
        except IngressoIndisponivel as e:
            self.__vendavisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__vendavisao.mostra_mensagem(f"Erro inesperado: {e}")

    def listar_vendas(self):
        vendas = self.__venda_DAO.get_all()  # Obtém todas as vendas
        if not vendas:  # Se não houver vendas, exibe uma mensagem
            self.__vendavisao.mostra_mensagem("Nenhuma venda realizada.")
        else:
            # Organiza os dados das vendas para exibição
            vendas_info = []
            for venda in vendas:
                try:
                    venda_info = {
                        "cliente_nome": venda.ingresso.cliente.nome,
                        "filme": venda.ingresso.sessao.filme.titulo,
                        "sala": venda.ingresso.sessao.sala.numero,
                        "horario_sessao": venda.ingresso.sessao.horario,
                        "horario_compra": venda.horario_compra.strftime("%Y-%m-%d %H:%M"),
                        "metodo_pagamento": venda.metodo_pagamento
                    }
                    vendas_info.append(venda_info)
                except Exception as e:
                    self.__vendavisao.mostra_mensagem(f"Erro ao processar a venda: {e}")

            # Exibe a lista de vendas formatada
            self.__vendavisao.exibe_lista_vendas(vendas_info)

    def atualizar_venda(self):
        try:
            vendas = self.__venda_DAO.get_all()
            self.listar_vendas()
            indice_venda = self.__vendavisao.seleciona_venda(vendas)

            if indice_venda is not None:
                venda = vendas[indice_venda]
                if datetime.now() > venda.ingresso.sessao.horario:
                    self.__vendavisao.mostra_mensagem("Venda não pode ser atualizada após o início da sessão.")
                    return

                novo_metodo_pagamento = self.__vendavisao.pega_metodo_pagamento()
                venda.metodo_pagamento = novo_metodo_pagamento
                self.__venda_DAO.update(venda)
                self.__vendavisao.mostra_mensagem(f"Método de pagamento atualizado para {venda.ingresso.cliente.nome}.")
            else:
                self.__vendavisao.mostra_mensagem("Nenhuma venda selecionada.")
        except Exception as e:
            self.__vendavisao.mostra_mensagem(f"Erro ao atualizar venda: {e}")

    def cancelar_venda(self):
        try:
            venda = self.obter_venda_por_indice()
            if not venda:
                return

            if datetime.now() > datetime.strptime(venda.ingresso.sessao.horario, "%H:%M"):
                self.__vendavisao.mostra_mensagem("Venda não pode ser cancelada após o início da sessão.")
                return

            self.__venda_DAO.remove(venda)
            venda.ingresso.sessao.ingressos_disponiveis += 1
            self.__vendavisao.mostra_mensagem(f"Venda cancelada para {venda.ingresso.cliente.nome}.")
        except Exception as e:
            self.__vendavisao.mostra_mensagem(f"Erro ao cancelar venda: {e}")

    def gerar_relatorio_vendas(self):
        vendas = self.__venda_DAO.get_all()
        total_vendas_por_filme = {}
        for venda in vendas:
            filme = venda.ingresso.sessao.filme.titulo
            total_vendas_por_filme[filme] = total_vendas_por_filme.get(filme, 0) + 1

        self.__vendavisao.mostra_relatorio_vendas(total_vendas_por_filme)
        
    def obter_venda_por_indice(self):
        vendas = self.__venda_DAO.get_all()
        self.listar_vendas()
        indice_venda = self.__vendavisao.seleciona_venda(vendas)

        if indice_venda is not None:
            return vendas[indice_venda]
        else:
            self.__vendavisao.mostra_mensagem("Nenhuma venda selecionada.")
            return None

    def abre_tela(self):
        lista_opcoes = {
            1: self.registrar_venda,
            2: self.listar_vendas,
            3: self.atualizar_venda,
            4: self.cancelar_venda,
            5: self.gerar_relatorio_vendas,
            0: self.retornar
        }

        continua = True
        while continua:
            opcao = self.__vendavisao.tela_opcoes()
            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.__vendavisao.mostra_mensagem("Opção inválida.")
