from controlador.cliente_controlador import ClienteControlador

class ClienteVisao:
    def __init__(self):
        self.controlador = ClienteControlador()

    def tela_opcoes(self):
        print("-------- GERENCIAMENTO DE CLIENTES ----------")
        print("Escolha a opção:")
        print("1 - Cadastrar Cliente")
        print("2 - Atualizar Cliente")
        print("3 - Remover Cliente")
        print("4 - Listar Clientes")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha a opção: "))
            if opcao not in [0, 1, 2, 3, 4]:
                raise ValueError("Opção inválida.")
        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um número válido.")
            return self.tela_opcoes()

        return opcao

    def pega_dados_cliente(self):
        nome = input("Nome do Cliente: ")
        fone = input("Telefone para Contato: ")
        email = input("Email: ").strip()  # Não converte para maiúsculas
        idade = input("Idade do Cliente: ")
        return {"nome": nome, "fone": fone, "email": email, "idade": idade}

    def mostra_cliente(self, cliente):
        print("-------- CLIENTE ----------")
        print(f"NOME: {cliente.nome}")
        print(f"TELEFONE: {cliente.fone}")
        print(f"EMAIL: {cliente.email}")
        print(f"IDADE: {cliente.idade}")
        print("\n")

    def seleciona_cliente(self):
        return input("Digite o nome do cliente que deseja selecionar: ")

    def mostra_mensagem(self, msg):
        print(msg)

    def listar_clientes(self, clientes):
        if isinstance(clientes, str):
            self.mostra_mensagem(clientes)
        else:
            if not clientes:
                self.mostra_mensagem("Nenhum cliente cadastrado.")
                return

            print("\nClientes cadastrados:")
            for cliente in clientes:
                self.mostra_cliente(cliente)
