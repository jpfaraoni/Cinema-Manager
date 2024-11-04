from entidade.cliente import Cliente

class ClienteVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("\n-------- GERENCIAMENTO DE CLIENTES ----------")
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
        print("\n===== CADASTRAR CLIENTE =====")
        nome = input("Nome do Cliente: ")
        fone = input("Telefone para Contato: ")
        email = input("Email: ").strip()  # Não converte para maiúsculas
        idade = int(input("Idade do Cliente: "))
        return {"nome": nome, "fone": fone, "email": email, "idade": idade}

    def mostra_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            print("Erro: O objeto fornecido não é um cliente válido.")
            return
        
        print("\n-------- CLIENTE ----------")
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
            return

        if not clientes:
            self.mostra_mensagem("Nenhum cliente cadastrado.")
            return

        print("\nClientes cadastrados:")
        for cliente in clientes:
            if isinstance(cliente, Cliente):
                self.mostra_cliente(cliente)
            else:
                print("Erro: Um dos itens na lista não é um cliente válido.")

    def mostra_confirmacao(self, acao):
        print(f"Cliente {acao} com sucesso!")
