from entidade.cliente import Cliente


class ClienteControlador:
    clientes_db = []  # Simulação do banco de dados em memória

    def cadastrar_cliente(self, nome, fone, email, idade):
        # Verifica se o cliente já está cadastrado
        for cliente in ClienteControlador.clientes_db:
            if cliente.nome == nome:
                return f"Cliente {nome} já está cadastrado(a)."

        # Tenta criar um novo cliente e adicionar ao banco de dados
        try:
            novo_cliente = Cliente(nome, fone, email, idade)
            ClienteControlador.clientes_db.append(novo_cliente)
            return f"Cliente {nome} foi adicionado(a) com sucesso!"
        except ValueError as e:
            return f"Erro ao cadastrar cliente: {e}"

    def atualizar_cliente(self, nome, fone=None, email=None, idade=None):
        # Procura pelo cliente e tenta atualizar suas informações
        for cliente in ClienteControlador.clientes_db:
            if cliente.nome == nome:
                try:
                    if fone is not None:
                        cliente.fone = fone
                    if email is not None:
                        cliente.email = email
                    if idade is not None:
                        cliente.idade = idade
                    return f"Cliente {nome} atualizado com sucesso."
                except ValueError as e:
                    return f"Erro ao atualizar cliente: {e}"
        return f"Cliente {nome} não encontrado."

    def remover_cliente(self, nome):
        # Remove o cliente do banco de dados, caso exista
        for cliente in ClienteControlador.clientes_db:
            if cliente.nome == nome:
                ClienteControlador.clientes_db.remove(cliente)
                return f"Cliente {nome} removido com sucesso."
        return f"Cliente {nome} não encontrado."

    def listar_clientes(self):
        # Retorna a lista de clientes ou uma mensagem se não houver clientes
        if not ClienteControlador.clientes_db:
            return "Nenhum cliente cadastrado."
        return [str(cliente) for cliente in ClienteControlador.clientes_db]
