import PySimpleGUI as sg
class FilmeVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        sg.change_look_and_feel('DarkGrey10')
        sg.change_look_and_feel('DarkGrey10')

        layout_esquerda = [
            [sg.Image(filename='visao/imagens/rb_60.png')]
        ]

        layout_direita = [
            [sg.Button("Adicionar Filme", key=1, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Atualizar Filme", key=2, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Remover Filme", key=3, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Listar Filmes", key=4, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Sair", key=0, size=(9, 1), font=("Helvetica", 12))],
        ]

        layout = [
            [sg.Column(layout_direita),
             sg.VSeparator(),
             sg.Column(layout_esquerda)]
        ]

        window = sg.Window("Menu Filme", layout, size=(600, 400), finalize=True)

        event, _ = window.read()
        window.close()
        return event if event is not None else 0

    def pega_dados_filme(self):
        layout = [
            [sg.Text("Título do filme:"), sg.InputText(key="titulo")],
            [sg.Text("Duração do filme (em minutos):"), sg.InputText(key="duracao")],
            [sg.Text("Gênero do filme:"), sg.InputText(key="genero")],
            [sg.Text("Classificação etária:"), sg.InputText(key="classificacao_etaria")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        window = sg.Window("Cadastrar Filme", layout)

        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return {
                "titulo": values["titulo"],
                "duracao": int(values["duracao"]),
                "genero": values["genero"],
                "classificacao_etaria": int(values["classificacao_etaria"]),
            }
        except ValueError:
            raise ValueError("Dados inválidos.")


    def pega_novos_dados_filme(self):
        layout = [
            [sg.Text("Nova duração do filme (em minutos):"), sg.InputText(key="duracao")],
            [sg.Text("Novo gênero do filme:"), sg.InputText(key="genero")],
            [sg.Text("Nova classificação etária:"), sg.InputText(key="classificacao_etaria")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Atualizar Filme", layout)

        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return {
                "duracao": int(values["duracao"]),
                "genero": values["genero"],
                "classificacao_etaria": int(values["classificacao_etaria"]),
            }
        except ValueError:
            raise ValueError("Dados inválidos.")

    def mostra_mensagem(self, msg):
        sg.popup(msg)

    def seleciona_filme(self):
        layout = [
            [sg.Text("Digite o título do filme que deseja selecionar:"), sg.InputText(key="titulo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Selecionar Filme", layout)

        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        return values["titulo"]

    def listar_filmes(self, filmes):
        if not filmes:
            sg.popup("Nenhum filme cadastrado.")
            return

        layout = [[sg.Text("Filmes cadastrados:")]]
        for filme in filmes:
            layout.append(
                [sg.Text(f"TÍTULO: {filme['titulo']}, DURAÇÃO: {filme['duracao']} min, GÊNERO: {filme['genero']}, "
                         f"CLASSIFICAÇÃO: {filme['classificacao_etaria']} anos")]
            )
        layout.append([sg.Button("Fechar")])

        window = sg.Window("Lista de Filmes", layout)
        window.read()
        window.close()
