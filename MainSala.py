from salacontrolador import SalaControlador
from salavisao import SalaVisao

def SalaMain():
    # Instanciando a visão
    visao = SalaVisao()  # Cria uma instância da visão

    # Loop principal para o menu da visão
    while True:
        opcao = visao.tela_opcoes()  # Exibe as opções e obtém a escolha do usuário

        if opcao == 0:
            print("Saindo do sistema.")
            break
        elif opcao == 1:
            # Adicionar sala
            visao.pega_dados_sala()  # A lógica de adicionar a sala e mostrar mensagens já está na visão
        elif opcao == 2:
            # Atualizar sala
            numero = visao.seleciona_sala()  # Seleciona a sala pelo número
            nova_capacidade = visao.pega_nova_capacidade()  # Solicita a nova capacidade
            resultado = visao.controlador.atualizar_sala(numero, capacidade=nova_capacidade)
            visao.mostra_mensagem(resultado)
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

