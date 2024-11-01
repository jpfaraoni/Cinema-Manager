
from filmecontrolador import FilmeControlador
from filmevisao import FilmeVisao

def FilmeMain():
    # Instanciando a visão
    visao = FilmeVisao()  # Cria uma instância da visão

    # Loop principal para o menu da visão
    while True:
        opcao = visao.tela_opcoes()  # Exibe as opções e obtém a escolha do usuário

        if opcao == 0:
            print("Saindo do sistema.")
            break
        elif opcao == 1:
            # Adicionar filme
            dados_filme = visao.pega_dados_filme()
            resultado = visao.controlador.adicionar_filme(dados_filme['titulo'], dados_filme['duracao'], dados_filme['genero'], dados_filme['classificacao_etaria'])
            visao.mostra_mensagem(resultado)
        elif opcao == 2:
            # Atualizar filme
            titulo = visao.seleciona_filme()
            dados_atualizados = visao.pega_dados_filme()  # Pede novos dados
            resultado = visao.controlador.atualizar_filme(titulo, duracao=dados_atualizados['duracao'], genero=dados_atualizados['genero'], classificacao_etaria=['classificacao_etaria'])
            visao.mostra_mensagem(resultado)
        elif opcao == 3:
            # Remover filme
            numero = visao.seleciona_filme()
            resultado = visao.controlador.remover_filme(titulo)
            visao.mostra_mensagem(resultado)
        elif opcao == 4:
            # Listar filmes
            resultado = visao.controlador.listar_filmes()  # Chama o método do controlador
            visao.listar_filmes(resultado)  # Passa o resultado para a visão
        else:
            visao.mostra_mensagem("Opção inválida.")

if __name__ == "__main__":
    main()
