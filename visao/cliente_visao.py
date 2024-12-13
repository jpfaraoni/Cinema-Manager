import PySimpleGUI as sg

class ClienteVisao:
    def tela_opcoes(self):
        sg.theme('DarkGrey10')
        layout = [
            [sg.Button("Cadastrar Cliente", key=1)],
            [sg.Button("Listar Clientes", key=2)],
            [sg.Button("Remover Cliente", key=3)],
            [sg.Button("Sair", key=0)]
        ]

        window = sg.Window("Menu Cliente", layout)
        event, _ = window.read()
        window.close()
        return event

    def pega_dados_cliente(self):
        sg.theme('DarkGrey10')
        layout = [
            [sg.Text("Nome:"), sg.InputText(key="nome")],
            [sg.Text("Telefone:"), sg.InputText(key="telefone")],
            [sg.Text("Email:"), sg.InputText(key="email")],
            [sg.Text("Idade:"), sg.InputText(key="idade")],
            [sg.Text("CPF:"), sg.InputText(key="cpf")],
            [sg.Button("Cadastrar", key="cadastrar")]
        ]

        window = sg.Window("Cadastrar Cliente", layout)
        event, values = window.read()
        window.close()

        if event == "cadastrar":
            return values
        return None

    def mostra_mensagem(self, mensagem):
        sg.Popup("Mensagem", mensagem)

    def exibe_lista_clientes(self, clientes):
        layout = [
            [sg.Text("Clientes Cadastrados")],
            [sg.Listbox(values=clientes, size=(50, 10))],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Lista de Clientes", layout)
        window.read()
        window.close()

    def pega_cpf_cliente(self):
        layout = [
            [sg.Text("CPF do Cliente:"), sg.InputText(key="cpf")],
            [sg.Button("Confirmar")]
        ]

        window = sg.Window("Remover Cliente", layout)
        event, values = window.read()
        window.close()
        return values["cpf"] if event == "Confirmar" else None

        window = sg.Window("Lista de Clientes", layout)
        event, _ = window.read()
        window.close()


    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Selecione um cliente para atualizar ou remover:")],
            [sg.InputText(key="nome"), sg.Button("Buscar", size=(10, 1), font=("Helvetica", 12))],
            [sg.Button("Fechar", size=(10, 1), font=("Helvetica", 12))]
        ]

        window = sg.Window("Seleção de Cliente", layout)
        event, values = window.read()
        window.close()

        if event == "Buscar" and values["nome"]:
            return values["nome"]
        self.mostra_mensagem("Cliente não encontrado.")
        return None


    def pega_novos_dados_cliente(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Novo Telefone:"), sg.InputText(key="telefone")],
            [sg.Text("Novo Email:"), sg.InputText(key="email")],
            [sg.Text("Nova Idade:"), sg.InputText(key="idade")],
            [sg.Text("Novo CPF:"), sg.InputText(key="cpf")],
            [sg.Button("Atualizar", size=(10, 1), font=("Helvetica", 12))]
        ]

        window = sg.Window("Atualizar Cliente", layout)
        event, values = window.read()
        window.close()

        if event == "Atualizar":
            return values["telefone"], values["email"], int(values["idade"]) if values["idade"].isdigit() else None, values["cpf"]
        return None
