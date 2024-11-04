from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self):
        self.pessoa = self

    @abstractmethod
    def obter_tipo_pessoa(self):
        pass

    @abstractmethod
    def __str__(self):
        pass