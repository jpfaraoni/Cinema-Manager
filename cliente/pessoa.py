from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, fone: str, email: str, idade: int):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not nome or not isinstance(nome, str):
            raise ValueError("Nome inválido. O nome não pode estar vazio e deve ser uma string.")
        self.__nome = nome

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone: str):
        if not fone or len(fone) < 10:
            raise ValueError("Telefone inválido. O telefone deve ter pelo menos 10 caracteres.")
        self.__fone = fone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Email inválido. Certifique-se de que o email contém '@' e um domínio válido.")
        self.__email = email

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Idade inválida. A idade deve ser um número inteiro positivo.")
        self.__idade = idade

    @abstractmethod
    def __str__(self):
        pass
