class Filme:

    filmes_db = []  # Simula um banco de dados de filmes

    def __init__(self, titulo: str, duracao: str, classificacao_etaria: int):
        self.__titulo = titulo
        self.__duracao = duracao
        self.__classificacao_etaria = classificacao_etaria

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: str):
        self.__duracao = duracao

    @property
    def classificacao_etaria(self):
        return self.__classificacao_etaria

    @classificacao_etaria.setter
    def classificacao_etaria(self, classificacao_etaria: int):
        self.__classificacao_etaria = classificacao_etaria

    @property
    def sinopse(self):
        return self.__sinopse

    @sinopse.setter
    def sinopse(self, sinopse: str):
        self.__sinopse = sinopse

    def adicionarFilme(self):
        """
        Aqui iremos adicionar o filme à uma lista de filmes para podermos utilizar essa lista posteriormente.
        Retorna uma confirmação: "filme(nome do filme) foi adicionado com sucesso!"
        """
        pass

    def atualizarFilme(self, titulo=None, duracao=None, genero=None, classificacao_etaria=None, sinopse=None):
        """
        Atualizaremos os dados de um determinado filme caso seja necessário (erro durante o cadastro de um filme por ex.).
        A atualização só ocorrerá caso os novos dados fornecidos existam (não forem Null).
        Retornará uma confirmação: "Filme atualizado: " seguido pelos novos dados do filme.
        """
        pass

    def removerFilme(self):
        """
        Método para remover um filme da nossa lista de filme, caso o filme que queremos remover pertença a lista de filmes.
        Esse método será utilizado pra, por exemplo, tirar um filme de cartaz>
        Retorna a confirmação com o nome do filme exluído caso ele exista.
        Retorna "Filme (nome do filme) não encontrado" caso o nome do filme fornecido não pertença a lista de filmes.
        """
        pass
