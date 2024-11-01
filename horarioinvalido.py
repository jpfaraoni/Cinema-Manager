class HorarioInvalido(Exception):
    """Exceção lançada quando o horário inserido pelo usuário é inválido."""
    def __init__(self, titulo_filme, sala, horario):
        super().__init__(f"O horário '{horario}' é inválido para o filme '{titulo_filme}' na sala '{sala}'. Use o formato HH:MM.")

