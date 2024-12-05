import PySimpleGUI as sg

class SalaVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        layout = [
            [sg.Text("-------- GERENCIAMENTO DE SALAS ----------", size=(30, 1))],
            [sg.Button("Adicionar Sala", key=1)],
            [sg.Button("Atualizar Sala", key=2)],
            [sg.Button("Remover Sala", key=3)],
            [sg.Button("Listar Salas", key=4)],
            [sg.Button("Sair", key=0)],
        ]
        window = sg.Window("Menu Principal - Salas", layout)

        event, _ = window.read()
        window.close()
        return event

    def pega_dados_sala(self):
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
            sg.popup("Erro: Dados inválidos.")
            return None

    def pega_novos_dados_sala(self):
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
            sg.popup("Erro: Capacidade inválida.")
            return None

    def seleciona_sala(self):
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
            sg.popup("Erro: Número inválido.")
            return None

    def mostra_mensagem(self, msg):
        sg.popup(msg)

    def exibe_lista_salas(self, salas):
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

