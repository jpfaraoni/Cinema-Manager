class VendaVisao:
    def tela_opcoes(self):
        print("\n-- Menu Vendas --")
        print("1. Realizar venda")
        print("2. Listar vendas")
        print("3. Atualizar venda")
        print("4. Cancelar venda")
        print("0. Sair")
        try:
            opcao = int(input("Escolha a opção: "))
            if opcao not in [0, 1, 2, 3, 4]:
                raise ValueError("Opção inválida.")
        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um número válido.")
            return self.tela_opcoes()  # Chama novamente para uma entrada correta

        return opcao

    def pega_dados_venda(self):
        print("\n===== REALIZAR VENDA =====")
        titulo = input("TÍTULO DO FILME: ")
        sala_numero = int(input("NÚMERO DA SALA: "))
        horario = input("HORÁRIO DA SESSÃO (HH:MM): ")

        print("Método de pagamento:")
        metodo_pagamento = input("Digite o método de pagamento (Cartão, Dinheiro, Pix): ")

        return {
            "titulo": titulo,
            "sala_numero": sala_numero,
            "horario": horario,
            "metodo_pagamento": metodo_pagamento
        }

    def seleciona_venda(self, vendas):
        try:
            if not vendas:
                print("Nenhuma venda disponível para seleção.")
                return None

            print("\n===== SELECIONE UMA VENDA =====")
            for index, venda in enumerate(vendas):
                print(f"{index}. Cliente: {venda.cliente.nome}, Filme: {venda.sessao.filme.titulo}")

            indice = int(input("Escolha o índice da venda: "))
            if indice < 0 or indice >= len(vendas):
                print("Índice inválido.")
                return None

            return indice
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return None

    def pega_metodo_pagamento(self):
        print("\n===== ATUALIZAR MÉTODO DE PAGAMENTO =====")
        novo_metodo_pagamento = input("Novo método de pagamento (1. Cartão, 2. Dinheiro, 3. Pix): ")
        return novo_metodo_pagamento

    def pega_dados_cancelamento(self):
        print("\n===== CANCELAR VENDA =====")
        confirmar = input("Tem certeza que deseja cancelar a venda? (s/n): ").lower()
        return confirmar == 's'

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_venda(self, dados_venda):
        print("\n===== DETALHES DA VENDA =====")
        print(f"Cliente: {dados_venda['cliente_nome']}")
        print(f"Filme: {dados_venda['filme']}")
        print(f"Sala: {dados_venda['sala']}")
        print(f"Horário da sessão: {dados_venda['horario_sessao']}")
        print(f"Horário da compra: {dados_venda['horario_compra']}")
        print(f"Método de pagamento: {dados_venda['metodo_pagamento']}\n")

    def mostra_relatorio_vendas(self, total_vendas_por_filme):
        print("\n===== RELATÓRIO DE VENDAS =====")
        if not total_vendas_por_filme:
            print("Nenhuma venda registrada.")
        else:
            for filme, total in total_vendas_por_filme.items():
                print(f"Filme: {filme} | Total de vendas: {total}")

    def mostra_confirmacao(self, acao):
        print(f"Venda {acao} com sucesso!")
