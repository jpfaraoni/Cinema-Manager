from visao.sessaovisao import SessaoVisao
from visao.vendavisao import VendaVisao
class ClienteInterface:
    def __init__(self):
       self.cliente_interface = None
       self.sessao_visao = SessaoVisao()
       self.venda_visao = VendaVisao()
    
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
