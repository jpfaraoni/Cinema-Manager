from horarioinvalido import HorarioInvalido
from sessaocontrolador import SessaoControlador
from filme import Filme
from filmevisao import FilmeVisao
from sala import Sala
from salavisao import SalaVisao
from sessao import Sessao

class SessaoVisao:
    """
    Classe de visão para gerenciar as interações com o usuário relacionadas às sessões.
    """

    def __init__(self):
        self.controlador = SessaoControlador()  # Associação com o controlador de sessões
        self.filme_visao = FilmeVisao()
        self.sala_visao = SalaVisao()
        self.sala = Sala(numero=None, capacidade=None, tipo=None)

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
        while True:
            try:
                # Entrada e validação do título e duração do filme
                filme = self.filme_visao.pega_dados_filme()

                # Entrada e validação da sala
                sala = self.sala_visao.pega_dados_sala()
                if self.sala.capacidade <= 0:
                    raise ValueError("A capacidade da sala deve ser um valor positivo.")

                # Entrada e validação do horário utilizando validar_horario
                horario = input("Digite o horário da sessão (HH:MM): ")
                self.controlador.validar_horario(horario)

                # Entrada e validação da capacidade máxima de ingressos
                capacidade_maxima = self.sala.capacidade
                if capacidade_maxima <= 0:
                    raise ValueError("A capacidade máxima deve ser um valor positivo.")

                tipo = Sessao.sala.tipo

                    # Cria a sessão e verifica disponibilidade do horário
                nova_sessao = Sessao(filme, sala, horario, capacidade_maxima, tipo)

                # Verifica se o horário está disponível
                if not self.controlador.horario_disponivel(nova_sessao):
                    print(f"Erro: Conflito de horário na sala {sala.numero} para o horário {horario}.")
                    continue  # Retorna ao início para nova entrada

                # Se chegarmos aqui, significa que o horário está disponível
                resultado = self.controlador.adicionar_sessao(filme, sala, horario, capacidade_maxima, tipo)
                print(resultado)  # Exibe a mensagem de sucesso
                return {"filme": filme, "sala": sala, "horario": horario, "capacidade_maxima": capacidade_maxima,
                        "tipo": tipo}

            except ValueError as ve:
                print(f"Erro de valor: {ve}. Tente novamente.")

            except HorarioInvalido:
                print("Horário inválido. Use o formato HH:MM.")

    # def pega_dados_sessao(self):
    #     filme = input("Digite o nome do filme: ")
    #     sala = int(input("Digite o número da sala: "))
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
    #         return {"filme": filme, "sala": sala, "horario": horario,
    #                 "ingressos_disponiveis": ingressos_disponiveis, "tipo": tipo}
    #     except ValueError as e:
    #         print(f"Erro: {e}. Tente novamente.")

        # except Exception as e:
        # # Captura outros erros de entrada de dados
        #     print(f"Erro: {e}. Por favor, insira os dados corretamente.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def exibe_lista_sessoes(self, sessoes_db):
        """
        Exibe a lista de sessões cadastradas.

        :param lista_sessoes: Lista de sessões a serem exibidas.
        """
        if isinstance(sessoes_db, str):
            self.mostra_mensagem(sessoes_db)  # Exibe mensagem de erro, se for uma string
        else:
            if not sessoes_db:  # Verifica se a lista de sessões está vazia
                self.mostra_mensagem("Nenhuma sessão cadastrada.")
                return

            print("\n-- Lista de Sessões --")
            for sessao in sessoes_db:
                # Acessa os atributos da sessão e imprime suas informações
                print(f"Filme: {sessao.filme.titulo}, "
                      f"Sala: {sessao.sala.numero}, "
                      f"Horário: {sessao.horario}, "
                      f"Capacidade: {sessao.capacidade_maxima}, "
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

    def pega_novos_dados_sessao(self):
        """
        Solicita ao usuário novos dados para a sessão.
        """
        try:
            capacidade_maxima = int(input("Digite a nova capacidade máxima: "))
            tipo = int(input("Digite o novo tipo (2D, 3D, ou IMAX): "))  # Exemplo de opções de tipo
            if tipo not in ["3D", "2D", "IMAX"]:
                raise ValueError("Tipo inválido. Escolha um número correspondente ao tipo de sessão.")

        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira valores válidos.")
            return self.pega_novos_dados_sessao()  # Chama novamente para uma entrada correta

        return {"capacidade_maxima": capacidade_maxima, "tipo": tipo}
