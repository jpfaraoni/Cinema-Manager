from cinema_interface import CinemaInterface  # Interface completa do gerente
from cliente_interface import ClienteInterface  # Interface limitada para o cliente

class SistemaCinema:
    def __init__(self):
        self.cinema_interface = CinemaInterface()
        self.cliente_interface = ClienteInterface()

    def tela_inicial(self):
        while True:
            print("\n--- Bem-vindo ao Sistema de Cinema ---")
            print("1. Entrar como Cliente")
            print("2. Entrar como Gerente")
            print("0. Sair")
            
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    self.cliente_interface.menu_cliente()
                elif opcao == 2:
                    self.autenticar_gerente()
                elif opcao == 0:
                    print("Saindo do sistema. Até logo!")
                    break
                else:
                    print("Opção inválida, tente novamente.")
            except ValueError:
                print("Erro: por favor, insira um número válido.")

    def autenticar_gerente(self):
        # Autenticação simples para proteger a interface de gerente
        senha = input("Digite a senha de acesso para o gerente: ")
        if senha == "senha123":  # Exemplo de senha; em um sistema real, use um método seguro
            print("Acesso concedido.")
            self.cinema_interface.menu_principal()
        else:
            print("Senha incorreta! Acesso negado.")

# Inicializa o sistema
if __name__ == "__main__":
    sistema = SistemaCinema()
    sistema.tela_inicial()
