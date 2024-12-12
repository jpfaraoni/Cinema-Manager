class SessaoNaoEncontrada(Exception):
    def __init__(self, codigo: int):
        super().__init__(f"Sessão não encontrada para o código {codigo}")
