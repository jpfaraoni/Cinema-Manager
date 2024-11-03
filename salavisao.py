class SalaVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("-------- GERENCIAMENTO DE SALAS ----------")
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
            print(f"Erro: {e}")
            return self.tela_opcoes()

        return opcao

    def pega_dados_sala(self):
        print("-------- DADOS DA SALA ----------")
        numero = int(input("Número da sala: "))
        capacidade = int(input("Capacidade da sala: "))

        return {"numero": numero, "capacidade": capacidade}

    def pega_novos_dados_sala(self):
        capacidade = int(input("Nova capacidade de sala: "))

        return(capacidade)


    def seleciona_sala(self):
        try:
            numero = int(input("Digite o número da sala que deseja selecionar: "))
        except ValueError:
            print("Erro: número inválido. Por favor, insira um número válido.")
            return self.seleciona_sala()

        return numero

    def mostra_mensagem(self, msg):
        print(msg)

    def exibe_lista_salas(self, salas):
        if not salas:
            self.mostra_mensagem("Nenhuma sala cadastrada.")
            return

        print("\nSalas cadastradas:")
        for sala in salas:
            print(f"NÚMERO: {sala['numero']}, CAPACIDADE: {sala['capacidade']}")
            print("\n")
