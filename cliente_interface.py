from mainSessao import sessaoMain
from mainCliente import clienteMain
from mainFilme import filmeMain
from mainSala import salaMain
class ClienteInterface:
    def __init__(self):
        self.main_sessao = sessaoMain()
        self.main_cliente = clienteMain()
        self.main_filme = filmeMain()
        self.main_sala = salaMain()
    
    def menu_cliente(self):
        while True:
            print("\n--- Menu Cliente ---")
            print("1. Listar Sessões Disponíveis")
            print("2. Comprar Ingresso")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.sessao_visao.listar_sessoes()
            elif opcao == "2":
                self.venda_visao.realizar_venda()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")
