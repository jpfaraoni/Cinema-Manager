import PySimpleGUI as sg

class SalaVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout_esquerda = [
            [sg.Image(filename='visao/imagens/rb_60.png')]
        ]

        layout_direita = [
        [sg.Button("Adicionar Sala", key=1, size=(10, 1), font=("Helvetica", 12))],
        [sg.Button("Atualizar Sala", key=2, size=(10, 1), font=("Helvetica", 12))],
        [sg.Button("Remover Sala", key=3, size=(10, 1), font=("Helvetica", 12))],
        [sg.Button("Listar Salas", key=4, size=(10, 1), font=("Helvetica", 12))],
        [sg.Button("Sair", key=0, size=(10, 1), font=("Helvetica", 12))],
        ]

        layout = [
            [sg.Column(layout_direita),
             sg.VSeparator(),
             sg.Column(layout_esquerda)]
        ]

        window = sg.Window("Menu Sala", layout)
        event, _ = window.read()
        window.close()
        # if event == sg.WINDOW_CLOSED:
        #     event = 0
        return event if event is not None else 0

    def pega_dados_sala(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Número da sala:"), sg.InputText(key="numero")],
            [sg.Text("Capacidade da sala:"), sg.InputText(key="capacidade")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Cadastrar Sala", layout)

        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return {
                "numero": int(values["numero"]),
                "capacidade": int(values["capacidade"]),
            }
        except ValueError:
            raise ValueError("Dados inválidos")

    def pega_novos_dados_sala(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Nova capacidade da sala:"), sg.InputText(key="capacidade")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Atualizar Sala", layout)

        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return int(values["capacidade"])
        except ValueError:
            raise ValueError("Dados inválidos.")

    def seleciona_sala(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Digite o número da sala que deseja selecionar:"), sg.InputText(key="numero")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Selecionar Sala", layout)

        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return int(values["numero"])
        except ValueError:
            raise ValueError("Dados inválidos.")

    def mostra_mensagem(self, msg):
        sg.ChangeLookAndFeel('DarkGrey10')
        sg.popup(msg)

    def exibe_lista_salas(self, salas):
        sg.ChangeLookAndFeel('DarkGrey10')
        if not salas:
            sg.popup("Nenhuma sala cadastrada.")
            return

        layout = [[sg.Text("Salas cadastradas:")]]
        for sala in salas:
            layout.append([sg.Text(f"NÚMERO: {sala['numero']}, CAPACIDADE: {sala['capacidade']}")])
        layout.append([sg.Button("Fechar")])

        window = sg.Window("Lista de Salas", layout)
        window.read()
        window.close()
