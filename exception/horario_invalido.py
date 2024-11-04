class HorarioInvalido(Exception):
    """Exceção lançada quando o horário inserido pelo usuário é inválido."""
    def __init__(self, horario):
        super().__init__(f"O horário '{horario}' é inválido. Use o formato HH:MM.")
