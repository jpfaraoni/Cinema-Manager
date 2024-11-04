from visao.sessao_visao import SessaoVisao


def main():
    # Instanciando a visão
    visao = SessaoVisao()  # Cria uma instância da visão

    # Loop principal para o menu da visão
    while True:
        opcao = visao.tela_opcoes()  # Exibe as opções e obtém a escolha do usuário

        if opcao == 0:
            print("Saindo do sistema.")
            break
        elif opcao == 1:
            # Adicionar sala
            visao.pega_dados_sessao()  # A lógica de adicionar a sala e mostrar mensagens já está na visão
        elif opcao == 2:
            # Atualizar sessao
            dados_sessao = visao.seleciona_sessao()  # Seleciona a sessão pelo filme, sala e horário
            dados_atualizados_sessao = visao.pega_dados_sessao()
            resultado = visao.controlador.atualizar_sessao(dados_atualizados_sessao["sessao"], dados_atualizados_sessao["filme"],
                                                           dados_atualizados_sessao["sala"], dados_atualizados_sessao["horario"],
                                                           dados_atualizados_sessao["capacidade_maxima"], dados_atualizados_sessao["tipo"])
            visao.mostra_mensagem(resultado)  # Mostra o resultado da operação
        elif opcao == 3:
            # Remover sessão
            dados_sessao = visao.seleciona_sessao()  # Seleciona a sessão a ser removida
            resultado = visao.controlador.remover_sessao(dados_sessao["filme"], dados_sessao["sala"], dados_sessao["horario"])
            visao.mostra_mensagem(resultado)  # Mostra o resultado da operação
        elif opcao == 4:
            # Listar sessões
            resultado = visao.controlador.listar_sessoes()  # Chama o método do controlador
            visao.exibe_lista_sessoes(resultado)  # Passa o resultado para a visão
        else:
            visao.mostra_mensagem("Opção inválida.")

if __name__ == "__main__":
    main()

