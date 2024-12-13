from abstrato.controlador_entidade_abstrata import ControladorEntidadeAbstrata
from exception.cliente_nao_encontrado import ClienteNaoEncontrado
from entidade.cliente import Cliente
from visao.cliente_visao import ClienteVisao
from DAO.cliente_dao import ClienteDAO

class ClienteControlador(ControladorEntidadeAbstrata):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__dao = ClienteDAO()
        self.__visao = ClienteVisao()

    def abre_tela(self):
        while True:
            opcao = self.__visao.tela_opcoes()

            if opcao == 1:  # Cadastrar Cliente
                dados = self.__visao.pega_dados_cliente()
                if dados:
                    try:
                        cliente = Cliente(
                            nome=dados["nome"],
                            telefone=dados["telefone"],
                            email=dados["email"],
                            idade=int(dados["idade"]),
                            cpf=dados["cpf"]
                        )
                        self.__dao.add(cliente)
                        self.__visao.mostra_mensagem("Cliente cadastrado com sucesso!")
                    except ValueError as e:
                        self.__visao.mostra_mensagem(str(e))

            elif opcao == 2:  # Listar Clientes
                clientes = [str(cliente) for cliente in self.__dao.get_all()]
                self.__visao.exibe_lista_clientes(clientes)

            elif opcao == 3:  # Remover Cliente
                cpf = self.__visao.pega_cpf_cliente()
                if cpf:
                    cliente = self.__dao.get(cpf)
                    if cliente:
                        self.__dao.remove(cpf)
                        self.__visao.mostra_mensagem("Cliente removido com sucesso!")
                    else:
                        self.__visao.mostra_mensagem("Cliente não encontrado!")

            elif opcao == 0:  # Sair
                break

# Programa Principal
if __name__ == "__main__":
    class ControladorSistema:
        def abre_tela(self):
            print("Retornando ao sistema principal...")

    controlador_sistema = ControladorSistema()
    controlador_cliente = ClienteControlador(controlador_sistema)
    controlador_cliente.abre_tela()


