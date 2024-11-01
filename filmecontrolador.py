from datetime import datetime, time
from filme import Filme, ClassificacaoEtaria

class FilmeControlador:
    filmes_db = []  # Simulação do banco de dados em memória

    def adicionar_filme(self, titulo: str, duracao: str, genero: str, classificacao_etaria: int):
        # Converte a duração para datetime.time
        try:
            horas, minutos = map(int, duracao.split(":"))
            duracao_time = time(horas, minutos)
        except ValueError:
            return "Formato de duração inválido. Use HH:MM."

        # Verifica se o filme já está cadastrado
        for filme in FilmeControlador.filmes_db:
            if filme.titulo == titulo:
                return f"Filme {titulo} já está cadastrado."

        # Cria e adiciona o novo filme
        novo_filme = Filme(titulo, duracao_time, genero, ClassificacaoEtaria(classificacao_etaria))
        FilmeControlador.filmes_db.append(novo_filme)
        return f"Filme {titulo} foi adicionado com sucesso!"

    def atualizar_filme(self, titulo: str, duracao: str = None, genero: str = None, classificacao_etaria: int = None):
        # Procura o filme pelo título e, se encontrado, atualiza seus atributos
        for filme in FilmeControlador.filmes_db:
            if filme.titulo == titulo:
                if duracao is not None:
                    try:
                        horas, minutos = map(int, duracao.split(":"))
                        filme.duracao = time(horas, minutos)
                    except ValueError:
                        return "Formato de duração inválido. Use HH:MM."
                if genero is not None:
                    filme.genero = genero
                if classificacao_etaria is not None:
                    filme.classificacao_etaria = ClassificacaoEtaria(classificacao_etaria)
                return f"Filme {titulo} atualizado com sucesso!"
        return f"Filme {titulo} não encontrado."

    def remover_filme(self, titulo: str):
        # Remove o filme do sistema, caso esteja cadastrado
        for filme in FilmeControlador.filmes_db:
            if filme.titulo == titulo:
                FilmeControlador.filmes_db.remove(filme)
                return f"Filme {titulo} foi removido com sucesso."
        return f"Filme {titulo} não encontrado."

    def listar_filmes(self):
        """
        Retorna a lista de filmes cadastrados.
        Se a lista estiver vazia, retorna uma mensagem de aviso.
        """
        if not FilmeControlador.filmes_db:
            return "Nenhum filme cadastrado."
        
        return FilmeControlador.filmes_db  # Retorna a lista de objetos filme
