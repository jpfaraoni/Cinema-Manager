import PySimpleGUI as sg

class SessaoVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkGrey10')

        layout_esquerda = [
            [sg.Image(filename='visao/imagens/rb_60.png')]
        ]

        layout_direita = [
            [sg.Button("Adicionar Sessão", key=1, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Atualizar Sessão", key=2, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Remover Sessão", key=3, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Listar Sessões", key=4, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Sair", key=5, size=(9, 1), font=("Helvetica", 12))],
        ]

        layout = [
            [sg.Column(layout_direita),
             sg.VSeparator(),
             sg.Column(layout_esquerda)]
        ]

        window = sg.Window("Menu Sessão", layout)

        event, _ = window.read()
        window.close()
        #key '5' = self.retornar
        return event if event is not None else 5

    def pega_dados_sessao(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("TÍTULO DO FILME:"), sg.InputText(key="titulo")],
            [sg.Text("NÚMERO DA SALA:"), sg.InputText(key="sala_numero")],
            [sg.Text("HORÁRIO DA SESSÃO (HH:MM):"), sg.InputText(key="horario")],
            [sg.Text("Escolha o tipo de sessão:")],
            [sg.Radio("2D", "TIPO", key="2D"), sg.Radio("3D", "TIPO", key="3D"),
            sg.Radio("IMAX", "TIPO", key="IMAX")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]

        window = sg.Window("Cadastrar Sessão", layout)
        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        tipo_selecionado = next((key for key, value in values.items() if key in ["2D", "3D", "IMAX"] and value), None)

        try:
            return {
                "titulo": values["titulo"],
                "sala_numero": int(values["sala_numero"]),
                "horario": values["horario"],
                "tipo": tipo_selecionado,
            }

        except ValueError:
            raise ValueError("Dados inválidos.")

    def mostra_mensagem(self, mensagem):
        sg.ChangeLookAndFeel('DarkGrey10')
        sg.popup(mensagem)

    def mostra_sessao(self, dados_sessao):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("TÍTULO: ", size=(15, 1)), sg.Text(dados_sessao["titulo"])],
            [sg.Text("SALA: ", size=(15, 1)), sg.Text(dados_sessao["numero_sala"])],
            [sg.Text("HORÁRIO: ", size=(15, 1)), sg.Text(dados_sessao["horario"])],
            [sg.Text("CÓDIGO: ", size=(15, 1)), sg.Text(dados_sessao["codigo"])],
            [sg.Text("TIPO: ", size=(15, 1)), sg.Text(dados_sessao["tipo"])],
            # [sg.Text("TIPO: ", size=(15, 1)), sg.Text(dados_sessao["tipo"].name)],
            [sg.Text("INGRESSOS DISPONÍVEIS: ", size=(15, 1)), sg.Text(dados_sessao["ingressos_disponiveis"])]
        ]
        layout.append([sg.Button("Fechar")])

        window = sg.Window("Detalhes da Sessão", layout)
        window.read()
        window.close()

    def seleciona_sessao(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Digite o código da sessão:"), sg.InputText(key="codigo")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]

        window = sg.Window("Selecionar Sessão", layout)
        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return int(values["codigo"])
        except ValueError:
            sg.popup("Erro: Código inválido.")
            return None

    def pega_novos_dados_sessao(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Nova capacidade máxima:"), sg.InputText(key="capacidade")],
            [sg.Text("Novo tipo de sessão:")],
            [sg.Radio(tipo.name, "TIPO", key=f"tipo_{tipo.value}") for tipo in TipoSessao],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]

        window = sg.Window("Atualizar Sessão", layout)
        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        tipo_selecionado = next((tipo for tipo in TipoSessao if values.get(f"tipo_{tipo.value}")), None)
        if not tipo_selecionado:
            raise ValueError("Tipo de sessão inválido.")

        return {
            "capacidade": int(values["capacidade"]),
            "tipo": tipo_selecionado,
        }


