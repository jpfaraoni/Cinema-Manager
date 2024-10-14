
from clientecontrolador import ClienteControlador
from clientevisao import ClienteVisao

def main():
    # Instanciando a visão
    visao = ClienteVisao()  # Cria uma instância da visão

    # Loop principal para o menu da visão
    while True:
        opcao = visao.tela_opcoes()  # Exibe as opções e obtém a escolha do usuário

        if opcao == 0:
            print("Saindo do sistema.")
            break
        elif opcao == 1:
            # Adicionar cliente
            dados_cliente = visao.pega_dados_cliente()
            resultado = visao.controlador.adicionar_cliente(dados_cliente['nome'], dados_cliente['fone'], dados_cliente['email'])
            visao.mostra_mensagem(resultado)
        elif opcao == 2:
            # Atualizar cliente
            numero = visao.seleciona_cliente()
            dados_atualizados = visao.pega_dados_cliente()  # Pede novos dados
            resultado = visao.controlador.atualizar_cliente(nome, fone=dados_atualizados['fone'], email=dados_atualizados['email'])
            visao.mostra_mensagem(resultado)
        elif opcao == 3:
            # Remover cliente
            numero = visao.seleciona_cliente()
            resultado = visao.controlador.remover_cliente(nome)
            visao.mostra_mensagem(resultado)
        elif opcao == 4:
            # Listar cliente
            resultado = visao.controlador.listar_clientes()  # Chama o método do controlador
            visao.listar_clientes(resultado)  # Passa o resultado para a visão
        else:
            visao.mostra_mensagem("Opção inválida.")

if __name__ == "__main__":
    main()
