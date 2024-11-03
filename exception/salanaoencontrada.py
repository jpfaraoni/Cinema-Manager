class SalaNaoEncontrada(Exception):
    """
    Exceção levantada quando uma sala não é encontrada no banco de dados.
    """
    def __init__(self, numero):
        super().__init__(f"Sala {numero} não foi encontrada.")
        self.numero = numero
