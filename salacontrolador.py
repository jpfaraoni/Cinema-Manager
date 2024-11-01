from sala import Sala
from salanaoencontrada import SalaNaoEncontrada

class SalaControlador:
    """
    Classe que controla as operações sobre o modelo Sala.

    Atributos:
    - salas_db: Lista que simula um banco de dados em memória para as salas.
    """

    salas_db = [] # Simulação do banco de dados em memória

    def adicionar_sala(self, numero, capacidade):
        """
        Adiciona uma nova sala se ela ainda não estiver cadastrada.

        :param numero: Número da sala.
        :param capacidade: Capacidade da sala.
        :return: Mensagem de sucesso ou erro.
        """
        # Verifica se a sala já existe
        for sala in SalaControlador.salas_db:
            if sala.numero == numero:
                raise ValueError(f"Sala {numero} já está cadastrada.")  # Levanta o erro

        # Caso não exista, adiciona a nova sala
        nova_sala = Sala(numero, capacidade)
        SalaControlador.salas_db.append(nova_sala)
        return f"Sala {numero} foi adicionada com sucesso!"

    def atualizar_sala(self, numero, capacidade=None):
        # Procura a sala pelo número e, se encontrada, atualiza seus atributos
        try:
            sala = self.busca_sala(numero)  # Chama o método busca_sala para encontrar a sala
            if capacidade is not None:
                sala.capacidade = capacidade  # Atualiza a capacidade
            return f"Sala {numero} atualizada com sucesso!"
        except SalaNaoEncontrada as e:
            return str(e)

    def busca_sala(self, numero):
        """
        Busca uma sala pelo número no banco de dados de salas.

        :param numero: Número da sala a ser buscada.
        :return: Objeto Sala se encontrado, senão levanta a exceção SalaNaoEncontrada.
        """
        for sala in SalaControlador.salas_db:
            if sala.numero == numero:
                return sala
        # Se a sala não for encontrada, levanta a exceção SalaNaoEncontrada
        raise SalaNaoEncontrada(numero)

    def remover_sala(self, numero):
        try:
            sala = self.busca_sala(numero)
            SalaControlador.salas_db.remove(sala)
            return f"Sala {numero} foi removida com sucesso."
        except SalaNaoEncontrada as e:
            return str(e)

    def listar_salas(self):
        """
        Retorna a lista de salas cadastradas.
        Se a lista estiver vazia, retorna uma mensagem de aviso.
        """
        if not SalaControlador.salas_db:
            return "Nenhuma sala cadastrada."

        return SalaControlador.salas_db  # Retorna a lista de objetos Sala
