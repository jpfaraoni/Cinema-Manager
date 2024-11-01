from salacontrolador import SalaControlador

class SalaVisao:
    def __init__(self):
        self.controlador = SalaControlador()  # Instancia do controlador

    def tela_opcoes(self):
        """
        Exibe as opções do menu principal para o gerenciamento de salas e retorna a opção escolhida.
        """
        print("-------- GERENCIAMENTO DE SALAS ----------")
        print("Escolha a opção:")
        print("1 - Adicionar Sala")
        print("2 - Atualizar Sala")
        print("3 - Remover Sala")
        print("4 - Listar Salas")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha a opção: "))
            if opcao not in [0, 1, 2, 3, 4]:
                raise ValueError("Opção inválida.")
        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um número válido.")
            return self.tela_opcoes()  # Chama novamente para uma entrada correta

        return opcao

    def pega_dados_sala(self):
        """
        Solicita os dados de uma sala ao usuário e retorna um dicionário com esses dados.
        """
        while True:  # Loop para garantir que o usuário digite dados válidos
            print("-------- DADOS DA SALA ----------")
            try:
                numero = int(input("Número da sala: "))
                capacidade = int(input("Capacidade da sala: "))
                tipo = input("Tipo da Sala: ")

                # Tenta adicionar a sala. Se der erro, é tratado.
                resultado = self.controlador.adicionar_sala(numero, capacidade, tipo)
                print(resultado)  # Exibe a mensagem de sucesso
                return {"numero": numero, "capacidade": capacidade}  # Retorna os dados da sala após sucesso

            except ValueError as e:
                # Captura o erro de sala já cadastrada
                print(f"Erro: {e}. Tente novamente.")
            except Exception as e:
                # Captura outros erros de entrada de dados
                print(f"Erro: {e}. Por favor, insira os dados corretamente.")

    def pega_nova_capacidade(self):
        """
        Solicita ao usuário a nova capacidade para atualizar a sala.
        """
        try:
            capacidade = int(input("Digite a nova capacidade da sala: "))
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira um número válido.")
            return self.pega_nova_capacidade()  # Chama novamente para uma entrada correta
        return capacidade

    def mostra_sala(self, dados_sala):
        """
        Exibe os dados de uma sala específica.
        """
        print("-------- SALA ----------")
        print(f"NÚMERO: {dados_sala.numero}")
        print(f"CAPACIDADE: {dados_sala.capacidade}")
        print("\n")

    def seleciona_sala(self):
        """
        Solicita ao usuário o número da sala que deseja selecionar e retorna esse número.
        """
        try:
            numero = int(input("Digite o número da sala que deseja selecionar: "))
        except ValueError:
            print("Erro: número inválido. Por favor, insira um número válido.")
            return self.seleciona_sala()  # Chama novamente para uma entrada correta

        return numero

    def mostra_mensagem(self, msg):
        """
        Exibe uma mensagem para o usuário.
        """
        print(msg)

    def exibe_lista_salas(self, salas):
        """
        Exibe a lista de salas cadastradas.

        :param salas: Lista de salas a serem exibidas.
        """
        if isinstance(salas, str):
            self.mostra_mensagem(salas)
        else:
            if not salas:  # Verifica se a lista de salas está vazia
                self.mostra_mensagem("Nenhuma sala cadastrada.")
                return

            print("\nSalas cadastradas:")
            for sala in salas:
                self.mostra_sala(sala)
            print("\nSalas cadastradas:")
            for sala in salas:
                self.mostra_sala(sala)
