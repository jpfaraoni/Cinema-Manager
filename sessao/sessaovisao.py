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
        """
        Exibe a lista de sessões cadastradas.

        :param lista_sessoes: Lista de sessões a serem exibidas.
        """
        if isinstance(lista_sessoes, str):
            self.mostra_mensagem(lista_sessoes)  # Exibe mensagem de erro, se for uma string
        else:
            if not lista_sessoes:  # Verifica se a lista de sessões está vazia
                self.mostra_mensagem("Nenhuma sessão cadastrada.")
                return

            print("\n-- Lista de Sessões --")
            for sessao in lista_sessoes:
                # Acessa os atributos da sessão e imprime suas informações
                print(f"Filme: {sessao.filme.titulo}, "
                      f"Sala: {sessao.sala}, "
                      f"Horário: {sessao.horario}, "
                      f"Ingressos Disponíveis: {sessao.ingressos_disponiveis}, "
                      f"Tipo: {sessao.tipo.name}")

    def exibe_lista_ingressos(self, ingressos):
        """
        Exibe a lista de ingressos vendidos.

        :param ingressos: Lista de ingressos a serem exibidos.
        """
        if isinstance(ingressos, str):
            self.mostra_mensagem(ingressos)  # Exibe mensagem de erro, se for uma string
        else:
            if not ingressos:  # Verifica se a lista de ingressos está vazia
                self.mostra_mensagem("Nenhum ingresso vendido.")
                return

            print("\nIngressos vendidos:")
            for ingresso in ingressos:
                # Assume que o ingresso possui atributos 'sessao' e 'cliente'
                print(f"Filme: {ingresso.sessao.filme.titulo}, "
                      f"Sala: {ingresso.sessao.sala}, "
                      f"Horário: {ingresso.sessao.horario}, "
                      f"Cliente: {ingresso.cliente.nome}")

    def seleciona_sessao(self):
        filme = input("Digite o nome do filme da sessão: ")
        sala = int(input("Digite o número da sala: "))
        horario = input("Digite o horário da sessão (HH:MM): ")
        return {"filme": filme, "sala": sala, "horario": horario}

    def pega_novos_dados_sessao(self):#TODO implementaçao esta errada, é necessario atualizar todos os atributos de sessao.
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
