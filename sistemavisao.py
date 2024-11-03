class SistemaVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("--------  ---------")
        print("+++++ ESCOLHA SUA OPÇÃO +++++")
        print("1 - Cadastro de Sala: ")
        print("2 - Cadastro de Filme: ")
        print("3 - Adicionar Sessão: ")
        print("0 - Finalizar sistema")

        try:
            opcao = int(input("Escolha a opção: "))
            if opcao not in [0, 1, 2, 3]:
                raise ValueError("Opção inválida.")
        except ValueError as e:
            print(f"Erro: {e}")
            return self.tela_opcoes()

        return opcao
