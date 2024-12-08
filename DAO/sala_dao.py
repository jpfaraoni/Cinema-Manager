from abstrato.dao import DAO
from entidade.sala import Sala

class SalaDAO(DAO):
    def __init__(self):
        super().__init__('salas.pkl')

    def add(self, sala: Sala):
        if isinstance(sala.numero, int) and (sala is not None) and isinstance(sala, Sala):
            super().add(sala.numero, sala)

    def update(self, sala: Sala):
        if((sala is not None) and isinstance(sala, Sala) and isinstance(sala.numero, int)):
            super().update(sala.numero, sala)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
