from abstrato.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, idade: int, cpf: str):
        self.nome = nome  # Usando o setter do nome
        self.telefone = telefone  # Usando o setter do telefone
        self.email = email  # Usando o setter do email
        self.idade = idade  # Usando o setter da idade
        self.cpf = cpf  # Usando o setter do CPF

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not nome or not isinstance(nome, str):
            raise ValueError("Nome inválido. O nome não pode estar vazio e deve ser uma string.")
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone: str):
        if not telefone or len(telefone) < 10:
            raise ValueError("Telefone inválido. O telefone deve ter pelo menos 10 caracteres.")
        self.__telefone = telefone

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
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: str):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido. O CPF deve ter 11 dígitos numéricos.")
        self.__cpf = cpf

    def obter_tipo_pessoa(self):
        return "Cliente"

    def __str__(self):
        return f"Cliente: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Idade: {self.idade}, CPF: {self.cpf}"
