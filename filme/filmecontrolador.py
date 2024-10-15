from filmemodelo import FilmeModelo

class FilmeControlador:
    filmes_db = []  # Simulação do banco de dados em memória

    def adicionar_filme(self, titulo: str, duracao: str, genero: str, classificacao_etaria: int, sinopse: str):
        # Adiciona um novo filme se ele ainda não estiver cadastrado
        for filme in FilmeControlador.filmes_db:
            if filme.titulo == titulo:
                return f"Filme {titulo} já está cadastrado."
        novo_filme = FilmeModelo(titulo, duracao, genero, classificacao_etaria, sinopse)
        FilmeControlador.filmes_db.append(novo_filme)
        return f"Filme {titulo} foi adicionado com sucesso!"

    def atualizar_filme(self, titulo: str, duracao: str, genero: str, classificacao_etaria: int, sinopse: str):
        # Procura o filme pelo titulo e, se encontrado, atualiza seus atributos
        for filme in FilmeControlador.filmes_db:
            if filme.titulo == titulo:
                if duracao is not None:
                    filme.duracao = duracao
                if genero is not None:
                    filme.genero = genero
                if classificacao_etaria is not None:
                    filme.classificacao_etaria = classificacao_etaria
                if sinopse is not None:
                    filme.sinopse = sinopse
                return f"Filme {titulo} atualizado com sucesso!"
        return f"Filme {titulo} não encontrado."

    def remover_filme(self, titulo: str, duracao: str, genero: str, classificacao_etaria: int, sinopse: str):
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

        return FilmeControlador.filmes_db  # Retorna a lista de objetos FilmeModelo
