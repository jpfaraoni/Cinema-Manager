import PySimpleGUI as sg

class SistemaVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        """
        Exibe a interface gráfica do menu principal do sistema.

        Retorna:
            int: Código da opção selecionada pelo usuário.
        """
        sg.ChangeLookAndFeel('DarkGrey10')
        layout_esquerda = [
            [sg.Image(filename='visao/imagens/rb_13067.png')]
        ]
        layout_direita = [
            [sg.Button("Salas", key=1, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Filmes", key=2, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Sessões", key=3, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Realizar Venda", key=4, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Cadastro Cliente", key=5, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Relatório", key=6, size=(9, 1), font=("Helvetica", 12))],
            [sg.Button("Finalizar Sistema", size=(9, 1), font=("Helvetica", 12))],
        ]

        layout = [
            [sg.Column(layout_direita),
            sg.VSeparator(),
            sg.Column(layout_esquerda)]
            ]
        # Cria a janela com o layout definido
        window = sg.Window("Menu Principal", layout, finalize=True)

        # Lê o evento do botão pressionado
        event, _ = window.read()
        window.close()

        # Retorna o código da opção selecionada
        return event if isinstance(event, int) else 0
