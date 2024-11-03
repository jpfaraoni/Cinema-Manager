from exception.horarioinvalido import HorarioInvalido
import re
from entidade.sessao import TipoSessao

class SessaoVisao:
    """
    Classe de visão para gerenciar as interações com o usuário relacionadas às sessões.
    """

    def __init__(self):
        pass
    # self.controlador = SessaoControlador

    def tela_opcoes(self):
        print("\n-- Menu Sessão --")
        print("1. Adicionar sessão")
        print("2. Atualizar sessão")
        print("3. Remover sessão")
        print("4. Listar sessões")
        print("0. Sair")
        try:
            opcao = int(input("Escolha a opção: "))
            if opcao not in [0, 1, 2, 3, 4]:
                raise ValueError("Opção inválida.")
        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um número válido.")
            return self.tela_opcoes()  # Chama novamente para uma entrada correta

        return opcao

    def pega_dados_sessao(self):
        try:
            print("===== ESCOLHA O FILME =====")
            titulo = input("TÍTULO DO FILME: ")

            print("===== ESCOLHA A SALA =====")
            sala_numero = int(input("NÚMERO DA SALA: "))

            print("===== DADOS DA SESSÃO =====")
            horario = input("Digite o horário da sessão (HH:MM): ")
            if not re.match(r'^\d{2}:\d{2}$', horario):
                raise HorarioInvalido(horario)

                # Verificação adicional para horas e minutos
            horas, minutos = map(int, horario.split(':'))
            if not (0 <= horas < 24 and 0 <= minutos < 60):
                raise HorarioInvalido(horario)

            # Escolha do tipo de sessão
            print("Escolha o tipo de sessão:")
            for tipo in TipoSessao:
                print(f"{tipo.value}. {tipo.name}")

            # tipo_escolhido = int(input("Digite o número correspondente ao tipo de sessão: "))
            # if tipo_escolhido not in [tipo.value for tipo in TipoSessao]:
            #     raise ValueError("Tipo de sessão inválido.")
            tipo_escolhido = int(input("Digite o número correspondente ao tipo de sessão: "))
            if tipo_escolhido in [tipo.value for tipo in TipoSessao]:
                tipo = TipoSessao(tipo_escolhido)
            else:
                raise ValueError("Tipo de sessão inválido.")

            return {"titulo": titulo, "sala_numero": sala_numero, "horario": horario, "tipo": tipo}

        except ValueError as ve:
            print(f"Erro de valor: {ve}. Tente novamente.")
        except HorarioInvalido as hi:
            print(hi)

    # def pega_dados_sessao(self):
    #     try:
    #         print("===== ESCOLHA O FILME =====")
    #         titulo = input("TÍTULO DO FILME: ")
    #
    #         print("===== ESCOLHA A SALA =====")
    #         sala_numero = int(input("NÚMERO DA SALA: "))
    #
    #         print("===== DADOS DA SESSÃO =====")
    #         horario = input("Digite o horário da sessão (HH:MM): ")
    #         if not re.match(r'^\d{2}:\d{2}$', horario):
    #             raise HorarioInvalido(horario)
    #
    #             # Verificação adicional para horas e minutos
    #         horas, minutos = map(int, horario.split(':'))
    #         if not (0 <= horas < 24 and 0 <= minutos < 60):
    #             raise HorarioInvalido(horario)
    #
    #         # Escolha do tipo de sessão
    #         print("Escolha o tipo de sessão:")
    #         for tipo in TipoSessao:
    #             print(f"{tipo.value}. {tipo.name}")
    #
    #         tipo_escolhido = int(input("Digite o número correspondente ao tipo de sessão: "))
    #         if tipo_escolhido not in [tipo.value for tipo in TipoSessao]:
    #             raise ValueError("Tipo de sessão inválido.")
    #
    #         return {"titulo": titulo, "sala_numero": sala_numero, "horario": horario, "tipo": tipo}
    #
    #     except ValueError as ve:
    #         print(f"Erro de valor: {ve}. Tente novamente.")
    #     except HorarioInvalido as hi:
    #         print(hi)

    # def pega_dados_sessao(self):
    #     controlador = input("Digite o nome do controlador: ")
    #     visao = int(input("Digite o número da visao: "))
    #     horario = input("Digite o horário da sessão (HH:MM): ")
    #     ingressos_disponiveis = int(input("Digite a quantidade de ingressos disponíveis: "))
    #
    #     # Exibe opções do Enum TipoSessao e captura a escolha do usuário
    #     print("Escolha o tipo de sessão:")
    #     try:
    #         for tipo in TipoSessao:
    #             print(f"{tipo.value}. {tipo.name}")
    #
    #         tipo_escolhido = int(input("Digite o número correspondente ao tipo de sessão: "))
    #         tipo = TipoSessao(tipo_escolhido)  # Converte a escolha para o tipo Enum
    #
    #         return {"controlador": controlador, "visao": visao, "horario": horario,
    #                 "ingressos_disponiveis": ingressos_disponiveis, "tipo": tipo}
    #     except ValueError as e:
    #         print(f"Erro: {e}. Tente novamente.")

        # except Exception as e:
        # # Captura outros erros de entrada de dados
        #     print(f"Erro: {e}. Por favor, insira os dados corretamente.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def mostra_sessao(self, dados_sessao):
        print("\n")
        print("TÍTULO: ", dados_sessao["titulo"])
        print("SALA: ", dados_sessao["numero_sala"])
        print("HORARIO: ", dados_sessao["horario"])
        print("TIPO: ", dados_sessao["tipo"].name)
        print("INGRESSOS DISPONIVEIS: ", dados_sessao["ingressos_disponiveis"])
        print("\n")

    # def exibe_lista_sessoes(self, sessoes_db):
    #     """
    #     Exibe a lista de sessões cadastradas.
    #
    #     :param lista_sessoes: Lista de sessões a serem exibidas.
    #     """
    #     if isinstance(sessoes_db, str):
    #         self.mostra_mensagem(sessoes_db)  # Exibe mensagem de erro, se for uma string
    #     else:
    #         if not sessoes_db:  # Verifica se a lista de sessões está vazia
    #             self.mostra_mensagem("Nenhuma sessão cadastrada.")
    #             return
    #
    #         print("\n-- Lista de Sessões --")
    #         for sessao in sessoes_db:
    #             # Acessa os atributos da sessão e imprime suas informações
    #             print(f"Filme: {sessao.filme.titulo}, "
    #                   f"Sala: {sessao.sala.numero}, "
    #                   f"Horário: {sessao.horario}, "
    #                   f"Capacidade: {sessao.sala.capacidade}, "
    #                   f"Tipo: {sessao.tipo.name}")


    def mostra_ingressos(self, ingressos):
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
                # Assume que o entidade possui atributos 'sessao' e 'cliente'
                print(f"Filme: {ingresso.sessao.filme.titulo}, "
                      f"Sala: {ingresso.sessao.sala}, "
                      f"Horário: {ingresso.sessao.horario}, "
                      f"Cliente: {ingresso.cliente.nome}")

    def seleciona_sessao(self):
        titulo = input("Digite o nome do titulo da sessão: ")
        sala_numero = int(input("Digite o número da sala: "))
        horario = input("Digite o horário da sessão (HH:MM): ")
        return {"titulo": titulo, "sala_numero": sala_numero, "horario": horario}

    def pega_novos_dados_sessao(self):
        """
        Solicita ao usuário novos dados para a sessão.
        """
        try:
            capacidade = int(input("Digite a nova capacidade máxima: "))
            tipo = int(input("Digite o novo tipo (1 - 2D, 2 - 3D, 3 - IMAX): "))  # Exemplo de opções de tipo
            if tipo not in [t.value for t in TipoSessao]:  # Supondo que TipoSessao seja um Enum
                raise ValueError("Tipo inválido. Escolha um número correspondente ao tipo de sessão.")
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira valores válidos.")
            return self.pega_novos_dados_sessao()  # Chama novamente para uma entrada correta

        return {"capacidade": capacidade, "tipo": TipoSessao(tipo)}
