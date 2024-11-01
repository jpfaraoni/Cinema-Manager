from clientevisao import ClienteVisao
from filmevisao import FilmeVisao
from clientevisao import ClienteVisao
from salavisao import SalaVisao
from sessaovisao import SessaoVisao
from sessaocontrolador import SessaoControlador 


class CinemaInterface:
    """
    Classe que representa a interface principal do sistema de gerenciamento de cinema.
    """
    def __init__(self):
        self.cinema_interface = None

    def menu_principal(self):
        while True:
            print("\n--- Sistema de Gerenciamento de Cinema ---")
            print("1. Gerenciar Filmes")
            print("2. Gerenciar Sessões")
            print("3. Gerenciar Clientes")
            print("4. Gerenciar Salas")
            print("5. Gerenciar Vendas")
            print("0. Sair")
            
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    self.menu_filmes()
                elif opcao == 2:
                    self.menu_sessoes()
                elif opcao == 3:
                    self.menu_clientes()
                elif opcao == 4:
                    self.menu_salas()
                elif opcao == 5:
                    self.menu_vendas()
                elif opcao == 0:
                    print("Saindo do sistema. Até logo!")
                    break
                else:
                    print("Opção inválida, tente novamente.")
            except ValueError:
                print("Erro: por favor, insira um número válido.")

    def menu_filmes(self):
        filme_visao = FilmeVisao()
        while True:
            opcao = filme_visao.tela_opcoes()  # Exibe as opções e obtém a escolha do usuário

            if opcao == 0:
                print("Saindo do gerenciamento de filmes.")
                break
            elif opcao == 1:
                # Adicionar filme
                dados_filme = filme_visao.pega_dados_filme()
                resultado = filme_visao.controlador.adicionar_filme(dados_filme['titulo'], dados_filme['duracao'], dados_filme['genero'], dados_filme['classificacao_etaria'])
                filme_visao.mostra_mensagem(resultado)
            elif opcao == 2:
                # Atualizar filme
                titulo = filme_visao.seleciona_filme()
                dados_atualizados = filme_visao.pega_dados_filme()  # Pede novos dados
                resultado = filme_visao.controlador.atualizar_filme(titulo, duracao=dados_atualizados['duracao'], genero=dados_atualizados['genero'], classificacao_etaria=['classificacao_etaria'])
                filme_visao.mostra_mensagem(resultado)
            elif opcao == 3:
                # Remover filme
                numero = filme_visao.seleciona_filme()
                resultado = filme_visao.controlador.remover_filme(titulo)
                filme_visao.mostra_mensagem(resultado)
            elif opcao == 4:
                # Listar filmes
                resultado = filme_visao.controlador.listar_filmes()  # Chama o método do controlador
                filme_visao.listar_filmes(resultado)  # Passa o resultado para a visão
            else:
                filme_visao.mostra_mensagem("Opção inválida.")

    def menu_sessoes(self):
        visao = SessaoVisao()  # Cria uma instância da visão
        controlador = SessaoControlador

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
                # Atualizar sessão
                dados_sessao = visao.seleciona_sessao()
                novos_dados = visao.pega_novos_dados_sessao()# Seleciona a sessão a ser removida
                resultado = visao.controlador.atualizar_sessao(filme = dados_sessao["filme"], sala = dados_sessao["sala"], horario = dados_sessao["horario"],
                                                            capacidade_maxima = novos_dados["capacidade_maxima"], tipo=novos_dados["tipo"])
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


    def menu_clientes(self):
        cliente_visao = ClienteVisao()

        while True:
            opcao = cliente_visao.tela_opcoes()

            if opcao == 0:
                print("Saindo do sistema.")
                break
            elif opcao == 1:
                dados_cliente = cliente_visao.pega_dados_cliente()
                resultado = cliente_visao.controlador.cadastrarCliente(dados_cliente['nome'], dados_cliente['fone'], dados_cliente['email'], dados_cliente['idade'])
                cliente_visao.mostra_mensagem(resultado)
            elif opcao == 2:
                nome = cliente_visao.seleciona_cliente()
                dados_atualizados = cliente_visao.pega_dados_cliente()
                resultado = cliente_visao.controlador.atualizarCliente(nome, fone=dados_atualizados['fone'], email=dados_atualizados['email'], idade=dados_atualizados['idade'])
                cliente_visao.mostra_mensagem(resultado)
            elif opcao == 3:
                nome = cliente_visao.seleciona_cliente()
                resultado = cliente_visao.controlador.removerCliente(nome)
                cliente_visao.mostra_mensagem(resultado)
            elif opcao == 4:
                resultado = cliente_visao.controlador.listar_clientes()
                cliente_visao.listar_clientes(resultado)

    def menu_salas(self):
        sala_visao = SalaVisao()  # Cria uma instância da visão

        while True:
            opcao = sala_visao.tela_opcoes()  # Exibe as opções e obtém a escolha do usuário

            if opcao == 0:
                print("Saindo do sistema.")
                break
            elif opcao == 1:
                # Adicionar sala
                sala_visao.pega_dados_sala()  # A lógica de adicionar a sala e mostrar mensagens já está na visão
            elif opcao == 2:
                # Atualizar sala
                numero = sala_visao.seleciona_sala()  # Seleciona a sala pelo número
                nova_capacidade = sala_visao.pega_nova_capacidade()  # Solicita a nova capacidade
                resultado = sala_visao.controlador.atualizar_sala(numero, capacidade=nova_capacidade)
                sala_visao.mostra_mensagem(resultado)
            elif opcao == 3:
                # Remover sala
                numero = sala_visao.seleciona_sala()
                resultado = sala_visao.controlador.remover_sala(numero)
                sala_visao.mostra_mensagem(resultado)
            elif opcao == 4:
                # Listar salas
                resultado = sala_visao.controlador.listar_salas()  # Chama o método do controlador
                sala_visao.exibe_lista_salas(resultado)  # Passa o resultado para a visão
            else:
                sala_visao.mostra_mensagem("Opção inválida.")
        
    def menu_vendas(self):
        while True:
            print("\n--- Gerenciamento de Vendas ---")
            print("1. Realizar Venda")
            print("2. Atualizar Método de Pagamento")
            print("3. Remover Venda")
            print("4. Listar Vendas")
            print("5. Calcular Total de Vendas")
            print("0. Voltar")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.venda_visao.realizar_venda()
            elif opcao == "2":
                self.venda_visao.atualizar_metodo_pagamento()
            elif opcao == "3":
                self.venda_visao.remover_venda()
            elif opcao == "4":
                self.venda_visao.listar_vendas()
            elif opcao == "5":
                self.venda_visao.calcular_total_vendas()
            elif opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

# Para iniciar o sistema
if __name__ == "__main__":
    interface = CinemaInterface()
    interface.menu_principal()
