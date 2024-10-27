class HorarioInvalido(Exception):
    """Exceção lançada quando o horário inserido pelo usuário é inválido."""
    def __init__(self, filme.titulo, sala, horario):
        super().__init__(f"O horário '{horario}' é inválido. Use o formato HH:MM.")
