import PySimpleGUI as sg
import re
from entidade.sessao import TipoSessao
from exception.horario_invalido import HorarioInvalido

class SessaoVisao:
    def __init__(self):
        pass

    def tela_opcoes(self):
        layout = [
            [sg.Text("-- Menu Sessão --", size=(30, 1))],
            [sg.Button("Adicionar Sessão", key=1)],
            [sg.Button("Atualizar Sessão", key=2)],
            [sg.Button("Remover Sessão", key=3)],
            [sg.Button("Listar Sessões", key=4)],
            [sg.Button("Sair", key=0)],
        ]
        window = sg.Window("Menu Sessão", layout)

        event, _ = window.read()
        window.close()
        return event

    def pega_dados_sessao(self):
        layout = [
            [sg.Text("TÍTULO DO FILME:"), sg.InputText(key="titulo")],
            [sg.Text("NÚMERO DA SALA:"), sg.InputText(key="sala_numero")],
            [sg.Text("HORÁRIO DA SESSÃO (HH:MM):"), sg.InputText(key="horario")],
            [sg.Text("Escolha o tipo de sessão:")],
            [sg.Radio(tipo.name.replace("_", ""), "TIPO", key=f"tipo_{tipo.value}") for tipo in TipoSessao],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]

        window = sg.Window("Cadastrar Sessão", layout)
        event, values = window.read()
        window.close()

        if event == "Cancelar" or event == sg.WINDOW_CLOSED:
            return None

        if not re.match(r'^\d{2}:\d{2}$', values["horario"]):
            raise HorarioInvalido(values["horario"])

        horas, minutos = map(int, values["horario"].split(":"))
        if not (0 <= horas < 24 and 0 <= minutos < 60):
            raise HorarioInvalido(values["horario"])

        tipo_selecionado = next((tipo for tipo in TipoSessao if values.get(f"tipo_{tipo.value}")), None)
        if not tipo_selecionado:
            raise ValueError("Tipo de sessão inválido.")

        return {
            "titulo": values["titulo"],
            "sala_numero": int(values["sala_numero"]),
            "horario": values["horario"],
            "tipo": tipo_selecionado,
        }

    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mostra_sessao(self, dados_sessao):
        layout = [
            [sg.Text("TÍTULO: ", size=(15, 1)), sg.Text(dados_sessao["titulo"])],
            [sg.Text("SALA: ", size=(15, 1)), sg.Text(dados_sessao["numero_sala"])],
            [sg.Text("HORÁRIO: ", size=(15, 1)), sg.Text(dados_sessao["horario"])],
            [sg.Text("CÓDIGO: ", size=(15, 1)), sg.Text(dados_sessao["codigo"])],
            [sg.Text("TIPO: ", size=(15, 1)), sg.Text(dados_sessao["tipo"].name)],
            [sg.Text("INGRESSOS DISPONÍVEIS: ", size=(15, 1)), sg.Text(dados_sessao["ingressos_disponiveis"])]
        ]
        layout.append([sg.Button("Fechar")])

        window = sg.Window("Detalhes da Sessão", layout)
        window.read()
        window.close()

    def mostra_ingressos(self, ingressos):
        if not ingressos:
            sg.popup("Nenhum ingresso vendido.")
            return

        layout = [[sg.Text("Ingressos vendidos:")]]
        for ingresso in ingressos:
            layout.append([
                sg.Text(f"Filme: {ingresso.sessao.filme.titulo}, Sala: {ingresso.sessao.sala}, \
                        Horário: {ingresso.sessao.horario}, Cliente: {ingresso.cliente.nome}")
            ])
        layout.append([sg.Button("Fechar")])

        window = sg.Window("Ingressos Vendidos", layout)
        window.read()
        window.close()

    def seleciona_sessao(self):
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
