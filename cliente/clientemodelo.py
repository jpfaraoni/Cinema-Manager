class ClienteModelo:
    def __init__(self, nome: str, fone: str, email: str):
        self.__nome = nome
        self.fone = fone  # Usando o setter
        self.email = email  # Usando o setter

    @property
    def nome(self):
        return self.__nome

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone: str):
        if not fone or len(fone) < 10:  # Validação simples
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
