from clientecontrolador import ClienteControlador

class ClienteVisao:
    """
    Classe que representa a interface com o usuário para gerenciar os clientes.
    """

    def __init__(self):
        self.controlador = ClienteControlador()  # Instancia do controlador

    def tela_opcoes(self):
        """
        Exibe as opções do menu principal para o gerenciamento de clientes e retorna a opção escolhida.
        """
        print("-------- GERENCIAMENTO DE CLIENTES ----------")
        print("Escolha a opção:")
        print("1 - Adicionar Cliente")
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
            return self.tela_opcoes()  # Chama novamente para uma entrada correta

        return opcao

    def pega_dados_cliente(self):
        """
        Solicita os dados de um cliente ao usuário e retorna um dicionário com esses dados.
        """
        print("-------- DADOS DO CLIENTE----------")

        nome = input("Nome do Cliente: ")
        fone = input("Telefone para Contato: ")
        email = input("Email: ").strip().upper()

        return {"nome": nome, "telefone": fone, "email": email}

    def mostra_cliente(self, dados_cliente):
        """
        Exibe os dados de um cliente específico.
        """
        print("-------- CLIENTE ----------")
        print(f"NOME: {dados_cliente.nome}")
        print(f"TELEFONE: {dados_cliente.fone}")
        print(f"EMAIL: {dados_cliente.email}")
        print("\n")

    def seleciona_cliente(self):
        """
        Solicita ao usuário o nome do cliente que deseja selecionar e retorna esse nome.
        """
        try:
            nome = input("Digite o nome do cliente que deseja selecionar: ")
        except ValueError:
            print("Erro: nome inválido. Por favor, insira um nome cadastrado.")
            return self.seleciona_cliente()  # Chama novamente para uma entrada correta

        return nome

    def mostra_mensagem(self, msg):
        """
        Exibe uma mensagem para o usuário.
        """
        print(msg)

    def listar_clientes(self, clientes):
        """
        Exibe a lista de clientes cadastrados.
        """
        if isinstance(clientes, str):  # Se a lista retornada for uma mensagem de erro
            self.mostra_mensagem(clientes)
        else:
            if not clientes:  # Verifica se a lista de salas está vazia
                self.mostra_mensagem("Nenhum clente cadastrado.")
                return

            print("\nClientes cadastrados:")
            for cliente in clietes:
                self.mostra_cliente(cliente)  # Passa cada objeto cliente diretamente
