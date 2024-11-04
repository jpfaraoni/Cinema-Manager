from controlador.sessao_controlador import SessaoControlador

class FilmeMaisAssistido:
    def __init__(self):
        self.controlador = SessaoControlador()

    def filme_mais_(self):
        contador_filmes = {}

        # Contagem de ingressos por controlador
        for sessao in self.controlador.sessoes_db:
            for ingresso in sessao.ingressos:  # Itera sobre a lista de ingressos na sessão
                filme = ingresso.sessao.filme  # Acessa o controlador associado ao entidade

                if filme.titulo not in contador_filmes:
                    contador_filmes[filme.titulo] = 0
                contador_filmes[filme.titulo] += 1  # Incrementa a contagem de ingressos para o controlador

        # Determinação do controlador mais assistido
        if contador_filmes:
            filme_mais_assistido = max(contador_filmes, key=contador_filmes.get)
            mensagem = f"O controlador mais assistido é '{filme_mais_assistido}' com {contador_filmes[filme_mais_assistido]} ingressos vendidos."
            return mensagem
        else:
            return "Nenhum controlador foi assistido."
