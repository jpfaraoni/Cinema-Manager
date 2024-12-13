class ClienteNaoEncontrado(Exception):
    def __init__(self, nome):
        super().__init__(f"Cliente {nome} não foi encontrado.")
        self.nome = nome