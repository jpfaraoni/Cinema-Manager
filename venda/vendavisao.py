from cliente import Cliente
from ingresso import Ingresso
from venda import Venda
from metodo_de_pagamento import MetodoDePagamento
from sessao import Sessao
from vendacontrolador import VendaControlador

class VendaVisao:
    """
    Classe de visão para gerenciar as interações com o usuário relacionadas às vendas de ingressos.
    """

    def __init__(self):
        self.controlador = VendaControlador()  # Associação com o controlador de vendas

    def tela_opcoes(self):
        print("\n-- Menu Vendas --")
        print("1. Realizar venda de ingresso")
        print("2. Listar vendas")
        print("3. Atualizar método de pagamento")
        print("4. Remover venda")
        print("5. Calcular total de vendas")
        print("0. Sair")
        try:
            opcao = int(input("Escolha a opção: "))
            if opcao not in [0, 1, 2, 3, 4, 5]:
                raise ValueError("Opção inválida.")
        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um número válido.")
            return self.tela_opcoes()  # Chama novamente para uma entrada correta

        return opcao

    def pega_dados_venda(self):
        try:
            # Dados do cliente
            nome_cliente = input("Digite o nome do cliente: ")
            cliente = Cliente(nome_cliente)

            # Dados da sessão
            filme = input("Digite o nome do filme: ")
            sala = int(input("Digite o número da sala: "))
            horario = input("Digite o horário da sessão (HH:MM): ")

            # Seleção do método de pagamento
            print("Escolha o método de pagamento:")
            for metodo in MetodoDePagamento:
                print(f"{metodo.value}. {metodo.name}")

            metodo_escolhido = int(input("Digite o número correspondente ao método de pagamento: "))
            if metodo_escolhido not in [metodo.value for metodo in MetodoDePagamento]:
                raise ValueError("Método de pagamento inválido.")
            metodo_pagamento = MetodoDePagamento(metodo_escolhido)

            # Chama a função de venda do controlador
            resultado = self.controlador.vender_ingresso(filme, sala, horario, cliente)
            print(resultado)  # Exibe a mensagem de sucesso ou erro
            return {"cliente": cliente, "filme": filme, "sala": sala, "horario": horario, "metodo_de_pagamento": metodo_pagamento}

        except ValueError as ve:
            print(f"Erro de valor: {ve}. Tente novamente.")

    def exibe_lista_vendas(self):
        vendas = self.controlador.listar_vendas()
        if isinstance(vendas, str):
            print(vendas)  # Exibe mensagem se não houver vendas
        else:
            print("\n-- Lista de Vendas --")
            for idx, venda in enumerate(vendas):
                print(f"ID: {idx}, Cliente: {venda.cliente.nome}, Filme: {venda.sessao.filme.titulo}, "
                      f"Sala: {venda.sessao.sala.numero}, Horário: {venda.sessao.horario}, "
                      f"Data da venda: {venda.data.strftime('%d/%m/%Y %H:%M:%S')}, "
                      f"Método de Pagamento: {venda.metodo_de_pagamento.name}")

    def atualizar_metodo_pagamento(self):
        try:
            venda_id = int(input("Digite o ID da venda para atualizar o método de pagamento: "))
            print("Escolha o novo método de pagamento:")
            for metodo in MetodoDePagamento:
                print(f"{metodo.value}. {metodo.name}")

            metodo_escolhido = int(input("Digite o número correspondente ao método de pagamento: "))
            if metodo_escolhido not in [metodo.value for metodo in MetodoDePagamento]:
                raise ValueError("Método de pagamento inválido.")
            novo_metodo = MetodoDePagamento(metodo_escolhido)

            resultado = self.controlador.atualizar_metodo_pagamento(venda_id, novo_metodo)
            print(resultado)
        except ValueError as ve:
            print(f"Erro de valor: {ve}. Tente novamente.")

    def remover_venda(self):
        try:
            venda_id = int(input("Digite o ID da venda a ser removida: "))
            resultado = self.controlador.remover_venda(venda_id)
            print(resultado)
        except ValueError:
            print("ID de venda inválido. Tente novamente.")

    def calcular_total_vendas(self):
        total = self.controlador.calcular_total_vendas()
        print(f"Total arrecadado em vendas: R$ {total:.2f}")
