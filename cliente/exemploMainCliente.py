from clientecontrolador import ClienteControlador
from clientevisao import ClienteVisao

def main():
    visao = ClienteVisao()

    while True:
        opcao = visao.tela_opcoes()

        if opcao == 0:
            print("Saindo do sistema.")
            break
        elif opcao == 1:
            dados_cliente = visao.pega_dados_cliente()
            resultado = visao.controlador.cadastrarCliente(dados_cliente['nome'], dados_cliente['fone'], dados_cliente['email'])
            visao.mostra_mensagem(resultado)
        elif opcao == 2:
            nome = visao.seleciona_cliente()
            dados_atualizados = visao.pega_dados_cliente()
            resultado = visao.controlador.atualizarCliente(nome, fone=dados_atualizados['fone'], email=dados_atualizados['email'])
            visao.mostra_mensagem(resultado)
        elif opcao == 3:
            nome = visao.seleciona_cliente()
            resultado = visao.controlador.removerCliente(nome)
            visao.mostra_mensagem(resultado)
        elif opcao == 4:
            resultado = visao.controlador.listar_clientes()
            visao.listar_clientes(resultado)

if __name__ == "__main__":
    main()
