class FilmeNaoEncontrado(Exception):
    def __init__(self, titulo):
        super().__init__(f"Filme '{titulo}' não foi encontrado.")
