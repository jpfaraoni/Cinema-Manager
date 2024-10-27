from sessaocontrolador import SessaoControlador
from sessaovisao import SessaoVisao

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
            sessao = controlador.busca_sessao(dados_sessao["filme"], dados_sessao["sala"], dados_sessao["horario"])
            novos_dados = visao.pega_novos_dados_sessao()  # Obtém novos dados para atualizar
            resultado = controlador.atualizar_sessao(sessao, **novos_dados)  # Atualiza a sessão
            visao.mostra_mensagem(resultado)  # Mostra o resultado da operação
        elif opcao == 3:
            # Remover sala
            numero = visao.seleciona_sala()
            resultado = visao.controlador.remover_sala(numero)
            visao.mostra_mensagem(resultado)
        elif opcao == 4:
            # Listar salas
            resultado = visao.controlador.listar_salas()  # Chama o método do controlador
            visao.exibe_lista_salas(resultado)  # Passa o resultado para a visão
        else:
            visao.mostra_mensagem("Opção inválida.")

if __name__ == "__main__":
    main()
