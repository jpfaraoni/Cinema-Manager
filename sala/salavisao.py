from salacontrolador import SalaControlador
from salacontrolador import TipoSala

class SalaVisao:
    """
    Classe que representa a interface com o usuário para gerenciar as salas.
    """

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
        print("-------- DADOS DA SALA ----------")
        try:
            numero = int(input("Número da sala: "))
            capacidade = int(input("Capacidade da sala: "))
            tipo_str = input("Tipo da sala (2D, 3D, IMAX): ").strip().upper()

            # Converte a entrada para o tipo de enumeração TipoSala
            try:
                tipo = TipoSala[f"_{tipo_str}"]
            except KeyError:
                raise ValueError("Tipo de sala inválido. Deve ser '2D', '3D' ou 'IMAX'.")

        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira os dados corretamente.")
            return self.pega_dados_sala()  # Chama novamente para uma entrada correta

        return {"numero": numero, "capacidade": capacidade, "tipo": tipo}  # Retorna os dados com tipo convertid

    def mostra_sala(self, dados_sala):
        """
        Exibe os dados de uma sala específica.
        """
        print("-------- SALA ----------")
        print(f"NÚMERO: {dados_sala.numero}")
        print(f"CAPACIDADE: {dados_sala.capacidade}")
        print(f"TIPO: {dados_sala.tipo}")
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

    def listar_salas(self, salas):
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
