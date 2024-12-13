from abstrato.controlador_entidade_abstrata import ControladorEntidadeAbstrata
from exception.cliente_nao_encontrado import ClienteNaoEncontrado
from entidade.cliente import Cliente
from visao.cliente_visao import ClienteVisao
from DAO.cliente_dao import ClienteDAO

class ClienteControlador(ControladorEntidadeAbstrata):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__clientes_db = []
        self.__clientevisao = ClienteVisao()
        self.__cliente_DAO = ClienteDAO()


    def cadastrar_cliente(self):
        try:
            dados_cliente = self.__clientevisao.pega_dados_cliente()
            if dados_cliente is not None:
                nome = dados_cliente["nome"]
                telefone = dados_cliente["telefone"]
                email = dados_cliente["email"]
                idade = dados_cliente["idade"]

                if not isinstance(nome, str):
                    raise ValueError(f"Nome precisa ser válido")
                if not isinstance(telefone, str):
                    raise ValueError(f"Telefone precisa ser válido")
                if not isinstance(email, str):
                    raise ValueError(f"Email precisa ser válido")
                if not isinstance(idade, int):
                    raise ValueError(f"Idade precisa ser válido")

                try:
                    self.busca_cliente(nome)  # Tenta buscar o filme pelo título
                    raise Exception(f"Cliente {nome} já está cadastrado.")
                except ClienteNaoEncontrado:
                    novo_cliente = Cliente(dados_cliente["nome"],dados_cliente["telefone"], 
                                           dados_cliente["email"], dados_cliente["idade"])
                    # USO DE DAO PARA SERIALIZAÇÃO
                    self.__cliente_DAO.add(novo_cliente)
                    self.__clientevisao.mostra_mensagem(f"Cliente {nome} foi adicionado com sucesso!")
        except ValueError as ve:
            self.__clientevisao.mostra_mensagem(f"Erro: {ve}")
        except Exception as e:
            self.__clientevisao.mostra_mensagem(f"Erro inesperado: {e}")

    def atualizar_cliente(self):
        try:
            self.lista_clientes()
            nome = self.__clientevisao.seleciona_cliente()
            if nome is None:
                return
            cliente = self.busca_cliente(nome)

            novos_dados = self.__clientevisao.pega_novos_dados_cliente()
            if novos_dados is None:
                return
            telefone, email, idade = novos_dados
            cliente.fone = telefone
            cliente.email = email
            cliente.idade = idade

            self.__cliente_DAO.update(cliente)
            self.__clientevisao.mostra_mensagem(f"Cliente {nome} atualizado com sucesso!")
        except ClienteNaoEncontrado as e:
            self.__clientevisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__clientevisao.mostra_mensagem(f"Erro inesperado: {e}")

    def busca_cliente(self, nome):
        clientes = self.__cliente_DAO.get_all()
        for cliente in clientes:
            if cliente.nome == nome:
                return cliente
        raise ClienteNaoEncontrado(nome)

    def remover_cliente(self):
        try:
            self.lista_clientes()
            nome = self.__clientevisao.seleciona_cliente()
            if nome is not None:
                cliente = self.busca_cliente(nome)
                self.__cliente_DAO.remove(nome)
                self.__clientevisao.mostra_mensagem(f"Cliente {nome} foi removido com sucesso.")
        except ClienteNaoEncontrado as e:
            self.__clientevisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__clientevisao.mostra_mensagem(f"Erro inesperado: {e}")

    def lista_clientes(self):
        clientes = self.__cliente_DAO.get_all()
        if not clientes:
            self.__clientevisao.mostra_mensagem("Nenhum cliente cadastrado.")
            return
        clientes_info = [{"nome": cliente.nome, "telefone": cliente.telefone, 
                          "email": cliente.email, "idade": cliente.idade} for cliente in clientes]
        self.__clientevisao.exibe_lista_clientes(clientes_info)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_cliente, 2: self.atualizar_cliente, 3: self.remover_cliente, 4: self.lista_clientes, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__clientevisao.tela_opcoes()]()

