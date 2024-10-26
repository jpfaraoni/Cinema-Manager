from sessao import Sessao, TipoSessao
from sessaonaoencontrada import SessaoNaoEncontrada
from ingresso import Ingresso


class SessaoControlador:
    """
    Controlador responsável por gerenciar as Sessões.

    Atributos:
    - sessoes_db: Simula o banco de dados em memória para as sessões.
    """

    sessoes_db = []

    def adicionar_sessao(self, filme, sala, horario, capacidade_maxima, tipo):
        if not isinstance(capacidade_maxima, int) or capacidade_maxima <= 0:
            raise ValueError("Capacidade máxima inválida.")

        if not isinstance(sala.tipo, TipoSala):
            raise ValueError("Tipo de sala inválido.")

        if tipo is not None and not isinstance(tipo, TipoSala):
            raise ValueError("Tipo de sessão inválido.")

        nova_sessao = Sessao(filme, sala, horario, capacidade_maxima, tipo)
        SessaoControlador.sessoes_db.append(nova_sessao)
        return f"Sessão do filme '{filme}' foi adicionada com sucesso!"

    def atualizar_sessao(self, sessao, filme=None, sala=None, horario=None, capacidade_maxima=None, tipo=None):
        if filme is not None:
            sessao.filme = filme

        if sala is not None and isinstance(sala.tipo, TipoSala):
            sessao.sala = sala

        if horario is not None:
            sessao.horario = horario

        if capacidade_maxima is not None:
            if isinstance(capacidade_maxima, int) and capacidade_maxima > 0:
                sessao.capacidade_maxima = capacidade_maxima
            else:
                raise ValueError("Capacidade máxima inválida.")

        if tipo is not None:
            if isinstance(tipo, TipoSala):
                sessao.tipo = tipo
            else:
                raise ValueError("Tipo de sessão inválido.")

        return f"Sessão do filme '{sessao.filme}' foi atualizada com sucesso!"

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

    def vender_ingresso(self, filme, sala, horario, cliente):
        sessao = self.busca_sessao(filme, sala, horario)
        if sessao.ingressos_disponiveis > 0:
            ingresso = Ingresso(sessao, cliente)
            sessao.Ingresso.ingressos_db.append(ingresso)  # Adiciona o ingresso à sessão
            return "Ingresso vendido com sucesso!"
        else:
            return "Capacidade máxima atingida, ingresso não pode ser vendido."

    def cancelarIngresso(self):
        """Cancela o ingresso, se vendido."""
        self.__sessao.__ingressos_disponiveis += 1
        self.ingressos_db.remove(self)
        print(f"Ingresso para o filme {self.__sessao.__filme} foi cancelado e está disponível novamente.")
        
    def emitirIngresso(self):
        """Marca o ingresso como vendido, se disponível."""
        if self.__sessao.__horario > time.now():
            if self.__sessao.__ingressos_diponiveis > 0:
                self.ingressos_db.append(self)
                self.__sessao.__ingresso_diponiveis -= 1
                print(f"Ingresso para o filme {self.__sessao.__filme} foi vendido.")
            else:
                print(f"Ingresso para o assento {self.__assento} já foi vendido.")
        else:
            print("Horário indisponível. Volte amanhã!")

