from sessao import Sessao
from sessaonaoencontrada import SessaoNaoEncontrada


class SessaoControlador:
    """
    Controlador responsável por gerenciar as Sessões.

    Atributos:
    - sessoes_db: Simula o banco de dados em memória para as sessões.
    """

    sessoes_db = []

    def adicionar_sessao(self, filme, sala, horario, ingressos_disponiveis, tipo):
        nova_sessao = Sessao(filme, sala, horario, ingressos_disponiveis, tipo)
        SessaoControlador.sessoes_db.append(nova_sessao)
        return f"Sessão do filme '{filme.titulo}' foi adicionada com sucesso!"

    def atualizar_sessao(self, filme, sala, horario, ingressos_disponiveis=None, tipo=None):
        try:
            sessao = self.busca_sessao(filme, sala, horario)
            sessao.atualizarSessao(filme=filme, sala=sala, horario=horario,
                                   ingressos_disponiveis=ingressos_disponiveis, tipo=tipo)
            return f"Sessão do filme '{filme.titulo}' foi atualizada com sucesso!"
        except SessaoNaoEncontrada as e:
            return str(e)

    def remover_sessao(self, filme, sala, horario):
        try:
            sessao = self.busca_sessao(filme, sala, horario)
            SessaoControlador.sessoes_db.remove(sessao)
            return f"Sessão do filme '{filme.titulo}' foi removida com sucesso."
        except SessaoNaoEncontrada as e:
            return str(e)

    def busca_sessao(self, filme, sala, horario):
        for sessao in SessaoControlador.sessoes_db:
            if sessao.filme == filme and sessao.sala == sala and sessao.horario == horario:
                return sessao
        raise SessaoNaoEncontrada(filme.titulo)

    def listar_sessoes(self):
        if not SessaoControlador.sessoes_db:
            return "Nenhuma sessão cadastrada."
        return SessaoControlador.sessoes_db
