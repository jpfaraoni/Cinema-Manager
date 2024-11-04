class SalaNaoEncontrada(Exception):
    def __init__(self, numero):
        super().__init__(f"Sala {numero} não foi encontrada.")
        self.numero = numero
