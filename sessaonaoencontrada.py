class SessaoNaoEncontrada(Exception):
    def __init__(self, titulo_filme, sala, horario):
        super().__init__(f"Sessão não encontrada para o filme '{titulo_filme}', sala {sala}, horário {horario}.")
