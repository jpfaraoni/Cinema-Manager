from abstrato.dao import DAO
from entidade.sessao import Sessao

class SessaoDAO(DAO):
    def __init__(self):
        super().__init__('sessoes.pkl')

    def add(self, sessao: Sessao):
        if isinstance(sessao.codigo, int) and (sessao is not None) and isinstance(sessao, Sessao):
            super().add(sessao.codigo, sessao)

    def update(self, sessao: Sessao):
        if((sessao is not None) and isinstance(sessao, Sessao) and isinstance(sessao.codigo, int)):
            super().update(sessao.codigo, sessao)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
