import PySimpleGUI as sg

class ClienteVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout_esquerda = [
            [sg.Image(filename='visao/imagens/rb_60.png')]
        ]

        layout_direita = [
            [sg.Button("Cadastrar Cliente", key=1, size=(10, 1), font=("Helvetica", 12))],
            [sg.Button("Atualizar Cliente", key=2, size=(10, 1), font=("Helvetica", 12))],
            [sg.Button("Remover Cliente", key=3, size=(10, 1), font=("Helvetica", 12))],
            [sg.Button("Listar Clientes", key=4, size=(10, 1), font=("Helvetica", 12))],
            [sg.Button("Sair", key=0, size=(10, 1), font=("Helvetica", 12))],
        ]

        layout = [
            [sg.Column(layout_direita),
             sg.VSeparator(),
             sg.Column(layout_esquerda)]
        ]

        window = sg.Window("Menu Cliente", layout)
        event, _ = window.read()
        window.close()
        return event if event is not None else 0

    def pega_dados_cliente(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Nome Cliente:"), sg.InputText(key="nome")],
            [sg.Text("Telefone Cliente:"), sg.InputText(key="telefone")],
            [sg.Text("Email Cliente:"), sg.InputText(key="email")],
            [sg.Text("Idade Cliente:"), sg.InputText(key="idade")],
            [sg.Text("CPF Cliente:"), sg.InputText(key="cpf")],
            [sg.Button("Cadastrar", size=(10, 1), font=("Helvetica", 12))]
        ]

        window = sg.Window("Cadastrar Cliente", layout)
        event, values = window.read()
        window.close()

        if event == "Cadastrar":
            if not values["nome"] or not values["telefone"] or not values["email"] or not values["idade"] or not values["cpf"]:
                self.mostra_mensagem("Por favor, preencha todos os campos.")
                return None
            return {
                "nome": values["nome"],
                "telefone": values["telefone"],
                "email": values["email"],
                "idade": int(values["idade"]) if values["idade"].isdigit() else None,
                "cpf": values["cpf"]
            }
        return None

    def mostra_mensagem(self, mensagem):
        sg.Popup("Mensagem", mensagem)

    def exibe_lista_clientes(self, lista_clientes):
        layout = [
            [sg.Text("Lista de Clientes", font=("Helvetica", 14))],
            [sg.Listbox([f"{cliente['nome']} - {cliente['telefone']} - {cliente['email']} - {cliente['cpf']} - {cliente['idade']} anos" 
                        for cliente in lista_clientes], size=(50, 10), key="lista_clientes")],
            [sg.Button("Fechar", size=(10, 1), font=("Helvetica", 12))]
        ]

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
