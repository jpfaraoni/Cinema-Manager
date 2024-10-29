from venda_controlador import VendaControlador
from metodo_de_pagamento import MetodoDePagamento

class VendaVisao:
    def __init__(self):
        self.controlador = VendaControlador()

    def mostrar_vendas(self):
        vendas = self.controlador.listar_vendas()
        if isinstance(vendas, str):
            print(vendas)
        else:
            for i, venda in enumerate(vendas):
                print(f"ID: {i}\n{venda}\n{'-' * 30}")

    def realizar_venda(self, cliente, ingressos, metodo_pagamento):
        try:
            if metodo_pagamento not in MetodoDePagamento:
                raise ValueError("Método de pagamento inválido.")
            mensagem = self.controlador.adicionar_venda(cliente, ingressos, metodo_pagamento)
            print(mensagem)
        except ValueError as ve:
            print(f"Erro: {ve}")

    def atualizar_metodo_pagamento(self, venda_id, novo_metodo_pagamento):
        try:
            if novo_metodo_pagamento not in MetodoDePagamento:
                raise ValueError("Método de pagamento inválido.")
            mensagem = self.controlador.atualizar_metodo_pagamento(venda_id, novo_metodo_pagamento)
            print(mensagem)
        except ValueError as ve:
            print(f"Erro: {ve}")

    def remover_venda(self, venda_id):
        mensagem = self.controlador.remover_venda(venda_id)
        print(mensagem)

    def mostrar_total_vendas(self):
        total = self.controlador.calcular_total_vendas()
        print(f"Total de vendas: R${total:.2f}")

