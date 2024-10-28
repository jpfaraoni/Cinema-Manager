class Cliente:
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
        try:
            if not nome or not isinstance(nome, str):
                raise ValueError("Nome inválido. O nome não pode estar vazio e deve ser uma string.")
            self.__nome = nome
        except ValueError as e:
            print(f"Erro ao definir nome: {e}")

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone: str):
        try:
            if not fone or len(fone) < 10:
                raise ValueError("Telefone inválido. O telefone deve ter pelo menos 10 caracteres.")
            self.__fone = fone
        except ValueError as e:
            print(f"Erro ao definir telefone: {e}")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        try:
            if '@' not in email or '.' not in email.split('@')[-1]:
                raise ValueError("Email inválido. Certifique-se de que o email contém '@' e um domínio válido.")
            self.__email = email
        except ValueError as e:
            print(f"Erro ao definir email: {e}")

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        try:
            if not isinstance(idade, int) or idade <= 0:
                raise ValueError("Idade inválida. A idade deve ser um número inteiro positivo.")
            self.__idade = idade
        except ValueError as e:
            print(f"Erro ao definir idade: {e}")

    def __str__(self):
        return f"Cliente: {self.nome}, Telefone: {self.fone}, Email: {self.email}, Idade: {self.idade}"
