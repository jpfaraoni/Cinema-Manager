from mainCliente import clienteMain
from mainFilme import filmeMain
from mainSessao import sessaoMain
from mainSala import salaMain

class CinemaInterface:
    """
    Classe que representa a interface principal do sistema de gerenciamento de cinema.
    """
    def __init__(self):
        self.main_filme = filmeMain()
        self.main_cliente = clienteMain()
        self.main_sessao = sessaoMain()
        self.main_sala = salaMain()

    def menu_principal(self):
        while True:
            print("\n--- Sistema de Gerenciamento de Cinema ---")
            print("1. Gerenciar Filmes")
            print("2. Gerenciar Sessões")
            print("3. Gerenciar Clientes")
            print("4. Gerenciar Salas")
            print("5. Gerenciar Vendas")
            print("0. Sair")
            
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    self.menu_filmes()
                elif opcao == 2:
                    self.menu_sessoes()
                elif opcao == 3:
                    self.menu_clientes()
                elif opcao == 4:
                    self.menu_salas()
                elif opcao == 5:
                    self.menu_vendas()
                elif opcao == 0:
                    print("Saindo do sistema. Até logo!")
                    break
                else:
                    print("Opção inválida, tente novamente.")
            except ValueError:
                print("Erro: por favor, insira um número válido.")

    def menu_filmes(self):
        while True:
            print("\n--- Gerenciamento de Filmes ---")
            print("1. Adicionar Filme")
            print("2. Remover Filme")
            print("3. Atualizar Filme")
            print("4. Listar Filmes")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.main_filme.adicionar_filme()
            elif opcao == "2":
                self.main_filme.remover_filme()
            elif opcao == "3":
                self.main_filme.atualizar_filme()
            elif opcao == "4":
                self.main_filme.listar_filmes()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

    def menu_sessoes(self):
        while True:
            print("\n--- Gerenciamento de Sessões ---")
            print("1. Adicionar Sessão")
            print("2. Remover Sessão")
            print("3. Atualizar Sessão")
            print("4. Listar Sessões")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.main_sessao.adicionar_sessao()
            elif opcao == "2":
                self.main_sessao.remover_sessao()
            elif opcao == "3":
                self.main_sessao.atualizar_sessao()
            elif opcao == "4":
                self.main_sessao.listar_sessoes()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

    def menu_clientes(self):
        while True:
            print("\n--- Gerenciamento de Clientes ---")
            print("1. Adicionar Cliente")
            print("2. Remover Cliente")
            print("3. Atualizar Cliente")
            print("4. Listar Clientes")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.main_cliente.adicionar_cliente()
            elif opcao == "2":
                self.main_cliente.remover_cliente()
            elif opcao == "3":
                self.main_cliente.atualizar_cliente()
            elif opcao == "4":
                self.main_cliente.listar_clientes()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

    def menu_salas(self):
        while True:
            print("\n--- Gerenciamento de Salas ---")
            print("1. Adicionar Sala")
            print("2. Remover Sala")
            print("3. Atualizar Sala")
            print("4. Listar Salas")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.main_sala.adicionar_sala()
            elif opcao == "2":
                self.main_sala.remover_sala()
            elif opcao == "3":
                self.main_sala.atualizar_sala()
            elif opcao == "4":
                self.main_sala.listar_salas()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

    def menu_vendas(self):
        while True:
            print("\n--- Gerenciamento de Vendas ---")
            print("1. Realizar Venda")
            print("2. Atualizar Método de Pagamento")
            print("3. Remover Venda")
            print("4. Listar Vendas")
            print("5. Calcular Total de Vendas")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.venda_visao.realizar_venda()
            elif opcao == "2":
                self.venda_visao.atualizar_metodo_pagamento()
            elif opcao == "3":
                self.venda_visao.remover_venda()
            elif opcao == "4":
                self.venda_visao.listar_vendas()
            elif opcao == "5":
                self.venda_visao.calcular_total_vendas()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

# Para iniciar o sistema
if __name__ == "__main__":
    interface = CinemaInterface()
    interface.menu_principal()
