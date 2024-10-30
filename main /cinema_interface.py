from filmevisao import FilmeVisao
from sessaovisao import SessaoVisao
from clientevisao import ClienteVisao
from salavisao import SalaVisao
from vendavisao import VendaVisao

class CinemaInterface:
    """
    Classe que representa a interface principal do sistema de gerenciamento de cinema.
    """
    def __init__(self):
        self.filme_visao = FilmeVisao()
        self.sessao_visao = SessaoVisao()
        self.cliente_visao = ClienteVisao()
        self.sala_visao = SalaVisao()
        self.venda_visao = VendaVisao()
        
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
            print("2. Atualizar Filme")
            print("3. Remover Filme")
            print("4. Listar Filmes")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.filme_visao.adicionar_filme()
            elif opcao == "2":
                self.filme_visao.atualizar_filme()
            elif opcao == "3":
                self.filme_visao.remover_filme()
            elif opcao == "4":
                self.filme_visao.listar_filmes()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

    def menu_sessoes(self):
        while True:
            print("\n--- Gerenciamento de Sessões ---")
            print("1. Adicionar Sessão")
            print("2. Atualizar Sessão")
            print("3. Remover Sessão")
            print("4. Listar Sessões")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.sessao_visao.adicionar_sessao()
            elif opcao == "2":
                self.sessao_visao.atualizar_sessao()
            elif opcao == "3":
                self.sessao_visao.remover_sessao()
            elif opcao == "4":
                self.sessao_visao.listar_sessoes()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

    def menu_clientes(self):
        while True:
            print("\n--- Gerenciamento de Clientes ---")
            print("1. Adicionar Cliente")
            print("2. Atualizar Cliente")
            print("3. Remover Cliente")
            print("4. Listar Clientes")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.cliente_visao.adicionar_cliente()
            elif opcao == "2":
                self.cliente_visao.atualizar_cliente()
            elif opcao == "3":
                self.cliente_visao.remover_cliente()
            elif opcao == "4":
                self.cliente_visao.listar_clientes()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

    def menu_salas(self):
        while True:
            print("\n--- Gerenciamento de Salas ---")
            print("1. Adicionar Sala")
            print("2. Atualizar Sala")
            print("3. Remover Sala")
            print("4. Listar Salas")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.sala_visao.adicionar_sala()
            elif opcao == "2":
                self.sala_visao.atualizar_sala()
            elif opcao == "3":
                self.sala_visao.remover_sala()
            elif opcao == "4":
                self.sala_visao.listar_salas()
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
