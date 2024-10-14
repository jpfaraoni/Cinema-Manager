class ClienteModelo:
    def __init__(self, nome: str, fone: str, email: str):
        self.__nome = nome
        self.__fone = fone
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def fone(self):
        return self.__fone

    @property
    def email(self):
        return self.__email
