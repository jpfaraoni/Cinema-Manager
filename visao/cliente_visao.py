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
        # if event == sg.WINDOW_CLOSED:
        #     event = 0
        return event if event is not None else 0
    
    def pega_dados_cliente(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Nome Cliente:"), sg.InputText(key="nome")],
            [sg.Text("Telefone para Contato:"), sg.InputText(key="telefone")],
            [sg.Text("Email:"), sg.InputText(key="email")],
            [sg.Text("Idade:"), sg.InputText(key="idade")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Cadastrar Cliente", layout)

        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return {
                "nome": str(values["nome"]),
                "telefone": str(values["telefone"]),
                "email": str(values["email"]),
                "idade": int(values["idade"]),
            }
        except ValueError:
            raise ValueError("Dados inválidos")

    def pega_novos_dados_cliente(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Novo telefone:"), sg.InputText(key="telefone")],
            [sg.Text("Novo email:"), sg.InputText(key="email")],
            [sg.Text("Nova idade:"), sg.InputText(key="idade")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Atualizar Cliente", layout)

        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return {
                "telefone": str(values["telefone"]),
                "email": str(values["email"]),
                "idade": int(values["idade"]),
            }
        except ValueError:
            raise ValueError("Dados inválidos.")


    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Digite o nome do cliente que deseja selecionar:"), sg.InputText(key="nome")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        window = sg.Window("Selecionar Cliente", layout)

        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return str(values["nome"])
        except ValueError:
            raise ValueError("Dados inválidos.")

    def mostra_mensagem(self, msg):
        sg.ChangeLookAndFeel('DarkGrey10')
        sg.popup(msg)

    def exibe_lista_clientes(self, clientes):
        sg.ChangeLookAndFeel('DarkGrey10')
        if not clientes:
            sg.popup("Nenhum cliente cadastrado.")
            return
        
        layout = [[sg.Text("Clientes cadastrados:")]]
        for cliente in clientes:
            layout.append([sg.Text(f"NOME: {cliente['nome']}, TELEFONE: {cliente['telefone']}, "
                                f"EMAIL: {cliente['email']}, IDADE: {cliente['idade']}")])
        layout.append([sg.Button("Fechar")])

        window = sg.Window("Lista de Clientes", layout)
        window.read()
        window.close()
