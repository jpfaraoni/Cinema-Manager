from filme import Filme
from sessao import Sessao
from sessaonaoencontrada import SessaoNaoEncontrada
#from ingresso import Ingresso
from datetime import datetime, timedelta


class SessaoControlador:
    """
    Controlador responsável por gerenciar as Sessões.

    Atributos:
    - sessoes_db: Simula o banco de dados em memória para as sessões.
    """

    sessoes_db = []
    ingressos = []

    def horario_disponivel(self, nova_sessao):
        """
        Verifica se há conflito entre o horário da nova sessão e as sessões já cadastradas,
        calculando o horário de término da sessão ao mesmo tempo.
        """
        # Valida o horário da nova sessão
        if not self.validar_horario(nova_sessao.horario):
            raise HorarioInvalido(nova_sessao.horario)

        novo_horario_inicio = datetime.strptime(nova_sessao.horario, "%H:%M")
        novo_horario_termino = novo_horario_inicio + timedelta(minutes=int(nova_sessao.filme.duracao))

        for sessao in SessaoControlador.sessoes_db:
            if sessao.sala == nova_sessao.sala:
                horario_inicio_existente = datetime.strptime(sessao.horario, "%H:%M")
                horario_termino_existente = horario_inicio_existente + timedelta(minutes=int(sessao.filme.duracao))

                # Verifica se há sobreposição de horários entre as sessões
                if (novo_horario_inicio < horario_termino_existente and
                        novo_horario_termino > horario_inicio_existente):
                    return False  # Conflito de horário
        return True  # Horário disponível

    def validar_horario(self, horario):
        """
        Valida se o horário está no formato HH:MM.
        Retorna True se o horário for válido, caso contrário, False.
        """
        try:
            datetime.strptime(horario, "%H:%M")
            return True
        except ValueError:
            return False

    def adicionar_ingresso(self, ingresso):
        SessaoControlador.ingressos.append(ingresso)  # Método para adicionar um ingresso

    def adicionar_sessao(self, filme, sala, horario, capacidade_maxima, tipo):
        if not isinstance(capacidade_maxima, int) or capacidade_maxima <= 0:
            raise ValueError("Capacidade máxima inválida.")

        # if sala is None or not isinstance(Sessao.tipo, TipoSessao):
        #     raise ValueError("Tipo de sala inválido.")

        # if tipo is not None and not isinstance(tipo, TipoSala):
        #     raise ValueError("Tipo de sessão inválido.")

        if not self.validar_horario(horario):
            raise HorarioInvalido(horario)

        # Se não houver conflito, adiciona a sessão ao "banco de dados"
        nova_sessao = Sessao(filme, sala, horario, capacidade_maxima, tipo)

        # Verifica se o horário é disponível
        if not self.horario_disponivel(nova_sessao):
            return f"Erro: Conflito de horário na sala {sala} para o horário {horario}."

        SessaoControlador.sessoes_db.append(nova_sessao)
        print(f"Sessão adicionada: {nova_sessao}")
        return f"Sessão do filme '{filme.titulo}' adicionada com sucesso!"

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

    def busca_sessao(self, filme:Filme, sala, horario):
        for sessao in SessaoControlador.sessoes_db:
            if sessao.filme == filme and sessao.sala == sala and sessao.horario == horario:
                return sessao
        raise SessaoNaoEncontrada(filme.titulo, sala, horario)

    def listar_sessoes(self):
        print("Sessoes cadastradas atualmente:", SessaoControlador.sessoes_db)
        if not SessaoControlador.sessoes_db:
            return "Nenhuma sessão cadastrada."
        return SessaoControlador.sessoes_db

    # def listar_ingressos(self):
    #     if not SessaoControlador.ingressos:
    #         return "Nenhum ingresso cadastrado."
    #     return SessaoControlador.ingressos
