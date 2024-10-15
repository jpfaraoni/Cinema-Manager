from salamodelo import SalaModelo


class SalaControlador:
    """
    Classe que controla as operações sobre o modelo Sala.

    Atributos:
    - salas_db: Lista que simula um banco de dados em memória para as salas.
    """

    salas_db = []  # Simulação do banco de dados em memória

    def adicionar_sala(self, numero, capacidade, tipo):
        # Adiciona uma nova sala se ela ainda não estiver cadastrada
        for sala in SalaControlador.salas_db:
            if sala.numero == numero:
                return f"Sala {numero} já está cadastrada."
        nova_sala = SalaModelo(numero, capacidade, tipo)
        SalaControlador.salas_db.append(nova_sala)
        return f"Sala {numero} foi adicionada com sucesso!"

    def atualizar_sala(self, numero, capacidade=None, tipo=None):
        # Procura a sala pelo número e, se encontrada, atualiza seus atributos
        for sala in SalaControlador.salas_db:
            if sala.numero == numero:
                if capacidade is not None:
                    sala.capacidade = capacidade
                if tipo is not None:
                    sala.tipo = tipo
                return f"Sala {numero} atualizada com sucesso!"
        return f"Sala {numero} não encontrada."

    def remover_sala(self, numero):
        # Remove a sala do sistema, caso esteja cadastrada
        for sala in SalaControlador.salas_db:
            if sala.numero == numero:
                SalaControlador.salas_db.remove(sala)
                return f"Sala {numero} foi removida com sucesso."
        return f"Sala {numero} não encontrada."

    def listar_salas(self):
        """
        Retorna a lista de salas cadastradas.
        Se a lista estiver vazia, retorna uma mensagem de aviso.
        """
        if not SalaControlador.salas_db:
            return "Nenhuma sala cadastrada."

        return SalaControlador.salas_db  # Retorna a lista de objetos SalaModelo
