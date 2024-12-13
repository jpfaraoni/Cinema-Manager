import PySimpleGUI as sg
from enum import Enum

import PySimpleGUI as sg
from enum import Enum

class MetodoDePagamento(Enum):
    DINHEIRO = "Dinheiro"
    CARTAO_CREDITO = "Cartão de Crédito"
    CARTAO_DEBITO = "Cartão de Débito"
    PIX = "Pix"

class VendaVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Button("Realizar Venda", key=1, size=(20, 1), font=("Helvetica", 12))],
            [sg.Button("Listar Vendas", key=2, size=(20, 1), font=("Helvetica", 12))],
            [sg.Button("Atualizar Venda", key=3, size=(20, 1), font=("Helvetica", 12))],
            [sg.Button("Cancelar Venda", key=4, size=(20, 1), font=("Helvetica", 12))],
            [sg.Button("Sair", key=0, size=(20, 1), font=("Helvetica", 12))],
        ]

        window = sg.Window("Menu Venda", layout)
        event, _ = window.read()
        window.close()
        return event if event is not None else 0

    def pega_dados_venda(self, sessao):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text(f"Título do Filme: {sessao.filme.titulo}")],
            [sg.Text(f"Número da Sala: {sessao.sala.numero}")],
            [sg.Text(f"Horário da Sessão: {sessao.horario}")],
            [sg.Text(f"Ingressos Disponíveis: {sessao.ingressos_disponiveis}")],
            [sg.Text("Método de Pagamento:")],
            sg.Combo([e.value for e in MetodoDePagamento], key="metodo_pagamento", readonly=True),
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Realizar Venda", layout)
        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return {
                "metodo_pagamento": values["metodo_pagamento"]
            }
        except ValueError:
            raise ValueError("Dados inválidos. Certifique-se de que os campos estão corretos.")

    def seleciona_venda(self, vendas):
        sg.ChangeLookAndFeel('DarkGrey10')
        if not vendas:
            sg.popup("Nenhuma venda disponível.")
            return None

        layout = [
            [sg.Text("Selecione a venda:")],
            [sg.Listbox(values=[f"Venda {i+1}: {v['titulo']} - {v['cliente']}" for i, v in enumerate(vendas)], 
                        size=(50, 10), key="venda_selecionada")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Venda", layout)
        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            selecionada = values["venda_selecionada"]
            if selecionada:
                return vendas[[f"Venda {i+1}: {v['titulo']} - {v['cliente']}" for i, v in enumerate(vendas)].index(selecionada[0])]
            else:
                raise ValueError("Nenhuma venda selecionada.")
        except ValueError:
            raise ValueError("Seleção inválida.")

    def mostra_mensagem(self, mensagem):
        sg.ChangeLookAndFeel('DarkGrey10')
        sg.popup(mensagem)

    def exibe_lista_vendas(self, vendas):
        sg.ChangeLookAndFeel('DarkGrey10')
        if not vendas:
            sg.popup("Nenhuma venda cadastrada.")
            return

        layout = [[sg.Text("Vendas cadastradas:")]]
        for venda in vendas:
            layout.append([sg.Text(f"Cliente: {venda['cliente']}, Filme: {venda['titulo']}, Preço: R${venda['preco']:.2f}")])
        layout.append([sg.Button("Fechar")])

        window = sg.Window("Lista de Vendas", layout)
        window.read()
        window.close()

    def pega_codigo_sessao(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Digite o código da sessão:")],
            [sg.InputText(key="codigo_sessao")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Sessão", layout)
        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        try:
            return int(values["codigo_sessao"])
        except ValueError:
            self.mostra_mensagem("Código inválido. Certifique-se de digitar um número.")
            return None
        
    def pega_cpf_cliente(self):
        sg.ChangeLookAndFeel('DarkGrey10')
        layout = [
            [sg.Text("Digite o CPF do Cliente:")],
            [sg.InputText(key="cpf_cliente")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Cliente", layout)
        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        cpf = values["cpf_cliente"]

        # Verificar se o CPF tem 11 dígitos numéricos
        if len(cpf) == 11 and cpf.isdigit():
            return cpf
        else:
            self.mostra_mensagem("CPF inválido. Certifique-se de digitar um CPF válido (11 dígitos).")
            return None
