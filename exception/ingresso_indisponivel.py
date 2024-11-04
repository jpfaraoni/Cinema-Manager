class IngressoIndisponivel(Exception):
    def __init__(self, sessao):
        super().__init__(f"Ingressos esgotados para a sessão do filme '{sessao.filme.titulo}' na sala {sessao.sala.numero} às {sessao.horario}.")
