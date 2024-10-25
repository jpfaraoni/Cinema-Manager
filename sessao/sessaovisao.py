from sessao import TipoSessao  # Importa o Enum TipoSessao para uso
from sessaocontrolador import SessaoControlador


class SessaoVisao:
    """
    Classe de visão para gerenciar as interações com o usuário relacionadas às sessões.
    """

    def __init__(self, controlador: SessaoControlador):
        self.controlador = controlador  # Associação com o controlador de sessões

    def tela_opcoes(self):
        print("\n-- Menu Sessão --")
        print("1. Adicionar sessão")
        print("2. Atualizar sessão")
        print("3. Remover sessão")
        print("4. Listar sessões")
        print("0. Sair")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def pega_dados_sessao(self):
        filme = input("Digite o nome do filme: ")
        sala = int(input("Digite o número da sala: "))
        horario = input("Digite o horário da sessão (HH:MM): ")
        ingressos_disponiveis = int(input("Digite a quantidade de ingressos disponíveis: "))

        # Exibe opções do Enum TipoSessao e captura a escolha do usuário
        print("Escolha o tipo de sessão:")
        for tipo in TipoSessao:
            print(f"{tipo.value}. {tipo.name}")

        tipo_escolhido = int(input("Digite o número correspondente ao tipo de sessão: "))
        tipo = TipoSessao(tipo_escolhido)  # Converte a escolha para o tipo Enum

        return {"filme": filme, "sala": sala, "horario": horario,
                "ingressos_disponiveis": ingressos_disponiveis, "tipo": tipo}

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def exibe_lista_sessoes(self, lista_sessoes):
        print("\n-- Lista de Sessões --")
        if isinstance(lista_sessoes, str):
            print(lista_sessoes)
        else:
            for sessao in lista_sessoes:
                print(f"Filme: {sessao.filme}, Sala: {sessao.sala}, Horário: {sessao.horario}, "
                      f"Ingressos Disponíveis: {sessao.ingressos_disponiveis}, Tipo: {sessao.tipo.name}")

    def seleciona_sessao(self):
        filme = input("Digite o nome do filme da sessão: ")
        sala = int(input("Digite o número da sala: "))
        horario = input("Digite o horário da sessão (HH:MM): ")
        return {"filme": filme, "sala": sala, "horario": horario}

    def pega_novos_dados_sessao(self):
        # Permite atualizar os dados da sessão
        ingressos_disponiveis = int(input("Digite a nova quantidade de ingressos disponíveis ou -1 para manter: "))

        # Exibe novamente as opções do Enum para escolha do tipo
        print("Escolha o novo tipo de sessão ou -1 para manter o atual:")
        for tipo in TipoSessao:
            print(f"{tipo.value}. {tipo.name}")

        tipo_escolhido = int(input("Digite o número correspondente ao novo tipo de sessão: "))
        tipo = TipoSessao(tipo_escolhido) if tipo_escolhido != -1 else None  # Ajusta para None se manter

        return {"ingressos_disponiveis": ingressos_disponiveis if ingressos_disponiveis != -1 else None,
                "tipo": tipo}
