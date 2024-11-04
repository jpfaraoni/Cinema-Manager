from entidade.venda import Venda, MetodoDePagamento
from entidade.cliente import Cliente
from entidade.ingresso import Ingresso
from entidade.sessao import Sessao
from datetime import datetime
from exception.sessaonaoencontrada import SessaoNaoEncontrada

class VendaControlador:
    vendas_db = []

    def vender_ingresso(self, filme, sala, horario, cliente, metodo_de_pagamento):
        try:
            sessao = self.busca_sessao(filme, sala, horario)

            if self.cliente.idade < sessao.filme.classificacao_etaria:
                return f"A idade do cliente ({self.cliente.idade} anos) é insuficiente para assistir a este filme (Classificação: {sessao.filme.classificacao_etaria} anos)."

            if sessao.ingressos_disponiveis > 0:
                ingresso = Ingresso(sessao, cliente)
                sessao.adicionar_ingresso(ingresso)
                nova_venda = Venda(cliente, [ingresso], metodo_de_pagamento)
                VendaControlador.vendas_db.append(nova_venda)

                return f"Venda de ingresso realizada para {cliente.nome} em {nova_venda.data.strftime('%d/%m/%Y %H:%M:%S')}."
            else:
                return "Capacidade máxima atingida, ingresso não pode ser vendido."

        except SessaoNaoEncontrada as e:
            return str(e)


    def listar_vendas(self):
        if not VendaControlador.vendas_db:
            return "Nenhuma venda realizada."
        return VendaControlador.vendas_db

    def atualizar_metodo_pagamento(self, venda_id: int, novo_metodo: MetodoDePagamento):
        try:
            venda = VendaControlador.vendas_db[venda_id]
            venda.metodo_de_pagamento = novo_metodo
            return f"Método de pagamento atualizado para {novo_metodo.value}."
        except IndexError:
            return f"Venda com ID {venda_id} não encontrada."
        except Exception as e:
            return str(e)

    def remover_venda(self, venda_id: int):
        try:
            venda = VendaControlador.vendas_db.pop(venda_id)
            return f"Venda para {venda.cliente.nome} em {venda.data.strftime('%d/%m/%Y %H:%M:%S')} foi removida."
        except IndexError:
            return f"Venda com ID {venda_id} não encontrada."

    def calcular_total_vendas(self):
        return sum(venda.preco_total for venda in VendaControlador.vendas_db)
