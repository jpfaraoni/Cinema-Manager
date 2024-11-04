from abstrato.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, fone: str, email: str, idade: int):
        super().__init__(nome, fone, email, idade)

    def __str__(self):
        return f"Cliente: {self.nome}, Telefone: {self.fone}, Email: {self.email}, Idade: {self.idade}"
