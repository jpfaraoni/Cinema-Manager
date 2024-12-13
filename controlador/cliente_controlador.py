from abstrato.controlador_entidade_abstrata import ControladorEntidadeAbstrata
from exception.cliente_nao_encontrado import ClienteNaoEncontrado
from entidade.cliente import Cliente
from visao.cliente_visao import ClienteVisao
from DAO.cliente_dao import ClienteDAO

class ClienteControlador(ControladorEntidadeAbstrata):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
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
                cpf = dados_cliente["cpf"]

                # Validações dos dados de entrada
                if not isinstance(nome, str) or not nome:
                    raise ValueError("Nome precisa ser válido.")
                if not isinstance(telefone, str) or not telefone:
                    raise ValueError("Telefone precisa ser válido.")
                if not isinstance(email, str) or not email:
                    raise ValueError("Email precisa ser válido.")
                if not isinstance(idade, int) or idade <= 0:
                    raise ValueError("Idade precisa ser válida e maior que zero.")
                if not isinstance(cpf, str) or len(cpf) != 11 or not cpf.isdigit():
                    raise ValueError("CPF precisa ser válido (11 dígitos numéricos).")

                try:
                    self.busca_cliente_por_cpf(cpf)  # Verifica se o CPF já existe
                    raise Exception(f"Cliente com CPF {cpf} já está cadastrado.")
                except ClienteNaoEncontrado:
                    novo_cliente = Cliente(nome, telefone, email, idade, cpf)
                    self.__cliente_DAO.add(novo_cliente)  # Adiciona cliente
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
            telefone, email, idade, cpf = novos_dados
            cliente.telefone = telefone
            cliente.email = email
            cliente.idade = idade
            cliente.cpf = cpf

            self.__cliente_DAO.update(cliente)  # Atualiza o cliente no DAO
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

    def busca_cliente_por_cpf(self, cpf):
        clientes = self.__cliente_DAO.get_all()
        for cliente in clientes:
            if cliente.cpf == cpf:
                return cliente
        raise ClienteNaoEncontrado(f"Cliente com CPF {cpf} não encontrado.")

    def remover_cliente(self):
        try:
            self.lista_clientes()
            nome = self.__clientevisao.seleciona_cliente()
            if nome is not None:
                cliente = self.busca_cliente(nome)
                self.__cliente_DAO.remove(cliente.cpf)  # Remove o cliente usando o CPF
                self.__clientevisao.mostra_mensagem(f"Cliente {nome} foi removido com sucesso.")
        except ClienteNaoEncontrado as e:
            self.__clientevisao.mostra_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__clientevisao.mostra_mensagem(f"Erro inesperado: {e}")

    def lista_clientes(self):
        clientes = self.__cliente_DAO.get_all()
        if not clientes:
            self.__clientevisao.mostra_mensagem("Nenhum cliente cadastrado.")
        else:
            clientes_info = [
                {
                    "nome": cliente.nome,
                    "telefone": cliente.telefone,
                    "email": cliente.email,
                    "cpf": cliente.cpf,
                    "idade": cliente.idade,
                } for cliente in clientes
            ]
            self.__clientevisao.exibe_lista_clientes(clientes_info)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_cliente, 2: self.atualizar_cliente, 3: self.remover_cliente, 4: self.lista_clientes, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__clientevisao.tela_opcoes()]()

    def obter_cliente_para_venda(self):
        """Método para obter o cliente ao fazer uma venda."""
        clientes = self.__cliente_DAO.get_all()
        if clientes:
            clientes_info = [
                {
                    "cpf": cliente.cpf,
                    "nome": cliente.nome
                } for cliente in clientes
            ]
            return clientes_info  # Retorna uma lista de clientes com CPF e nome para exibir na venda
        else:
            self.__clientevisao.mostra_mensagem("Nenhum cliente encontrado!")
            return []

