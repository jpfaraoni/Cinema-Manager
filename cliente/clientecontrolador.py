from cliente import Cliente


class ClienteControlador:
    clientes_db = []  # Simulação do banco de dados em memória

    def cadastrarCliente(self, nome, fone, email):
        for cliente in ClienteControlador.clientes_db:
            if cliente.nome == nome:
                return f"Cliente {nome} já está cadastrado(a)."

        novo_cliente = ClienteModelo(nome, fone, email)
        ClienteControlador.clientes_db.append(novo_cliente)
        return f"Cliente {nome} foi adicionado(a) com sucesso!"

    def atualizarCliente(self, nome, fone=None, email=None):
        for cliente in ClienteControlador.clientes_db:
            if cliente.nome == nome:
                if fone is not None:
                    cliente.fone = fone
                if email is not None:
                    cliente.email = email
                return f"Cliente {nome} atualizado com sucesso."
        return f"Cliente {nome} não encontrado."

    def removerCliente(self, nome):
        for cliente in ClienteControlador.clientes_db:
            if cliente.nome == nome:
                ClienteControlador.clientes_db.remove(cliente)
                return f"Cliente {nome} removido com sucesso."
        return f"Cliente {nome} não encontrado."

    def listar_clientes(self):
        if not ClienteControlador.clientes_db:
            return "Nenhum cliente cadastrado."
        return ClienteControlador.clientes_db
