class Cliente:
    def __init__(self, nome: str, fone: str, email: str):
        self.nome = nome
        self.fone = fone
        self.email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not nome or not isinstance(nome, str):
            raise ValueError("Digite um nome válido.")
        self.__nome = nome

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone: str):
        if not fone or len(fone) < 10:
            raise ValueError("Telefone deve ter pelo menos 10 caracteres.")
        self.__fone = fone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Email inválido.")
        self.__email = email

    def __str__(self):
        return f"Cliente: {self.nome}, Telefone: {self.fone}, Email: {self.email}"



### Fazer tratamento de excessao na entrada de dados
