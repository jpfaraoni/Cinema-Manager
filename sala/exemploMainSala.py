from salacontrolador import SalaControlador
from salavisao import SalaVisao

def main():
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
            dados_sala = visao.pega_dados_sala()
            resultado = visao.controlador.adicionar_sala(dados_sala['numero'], dados_sala['capacidade'], dados_sala['tipo'])
            visao.mostra_mensagem(resultado)
        elif opcao == 2:
            # Atualizar sala
            numero = visao.seleciona_sala()
            dados_atualizados = visao.pega_dados_sala()  # Pede novos dados
            resultado = visao.controlador.atualizar_sala(numero, capacidade=dados_atualizados['capacidade'], tipo=dados_atualizados['tipo'])
            visao.mostra_mensagem(resultado)
        elif opcao == 3:
            # Remover sala
            numero = visao.seleciona_sala()
            resultado = visao.controlador.remover_sala(numero)
            visao.mostra_mensagem(resultado)
        elif opcao == 4:
            # Listar salas
            resultado = visao.controlador.listar_salas()  # Chama o método do controlador
            visao.listar_salas(resultado)  # Passa o resultado para a visão
        else:
            visao.mostra_mensagem("Opção inválida.")

if __name__ == "__main__":
    main()
