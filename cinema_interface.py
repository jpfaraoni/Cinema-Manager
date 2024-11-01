from mainFilme import filmeMain
from mainCliente import clienteMain
from mainSala import salaMain
from mainSessao import sessaoMain

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
        self.main_filme()
        
    def menu_sessoes(self):
        self.main_sessao()
        
    def menu_clientes(self):
        self.main_cliente()
    
    def menu_salas(self):
        self.main_sala()
    
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
if __name__ == "__mainPrincipal__":
    interface = CinemaInterface()
    interface.menu_principal()
