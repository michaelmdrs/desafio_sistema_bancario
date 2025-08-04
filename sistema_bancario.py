import datetime, time


def movimentacao():
    def mensagem():
        print(65 * "=")
        txt = 'SISTEMA ONBANK ONLINE'
        print(txt.center(60).upper())
        print(65 * '=')
        menu_text = 'MENU ONBANK'
        frase = 'Escolha a opção desejada'
        print(menu_text.center(65).upper())
        print(frase.center(65).upper())
        print()
        menu = 'CADASTRO [1] | SAQUE [2] | DEPÓSITO [3] | EXTRATO [4] | SAIR [5]'
        print(menu.center(65).upper())
        print(65 * '=')


    def log_transacoes(func):
        def wrapper(*args, **kwargs):
            hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            resultado = func(*args, **kwargs)
            print(f'\n[LOG] Transação: {func.__name__.upper()} | Data e Hora: {hora}')
            return  resultado
        return wrapper


    @log_transacoes
    def saque(saldo):
        valor = float(input('Digite o valor do saque: '))
        if valor <= 0:
            print('Valor inválido. Saque não realizado.')
            return saldo, None,
        elif valor > 500:
            print('Valor acima do permitido (R$ 500.00). Saque não realizado.')
            return saldo, None
        elif valor > saldo:
            print('Saldo insuficiente. Saque não realizado.')
            return saldo, None
        else:
            saldo -= valor
            print('Saque realizado com sucesso.')
            print(f'O valor do saque foi de R${valor:.2f}')
            return saldo, valor
    @log_transacoes
    def deposito(saldo):
        valor = float(input('Digite o valor do depósito: '))
        if valor <= 0:
            print('Valor inválido. Depósito não realizado.')
            return saldo, None
        else:
            saldo += valor
            print('Depósito realizado com sucesso.')
            print(f'O valor do depósito foi de R${valor:.2f}')
            return saldo, valor


    @log_transacoes
    def cadastro():
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF: ')
        data_nascimento = input('Digite sua data de nascimento: ')
        print('Cadastro realizado com sucesso')


    @log_transacoes
    def sair():
        time.sleep(3)
        print("Saindo do sistema. Obrigado por usar o ONBANK ONLINE!")


    @log_transacoes
    def extrato(saldo, transacoes):
        print("\n================ EXTRATO ================")
        if not transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in transacoes:
                print(transacao)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==========================================")

    menu_opcao = {
        1: cadastro,
        2: saque,
        3: deposito,
        4: extrato,
        5: sair
    }

    saldo = 0
    transacoes = []
    LIMITE_SAQUE = 3
    saques_realizados_hoje = 0


    while True:
        try:
            mensagem()
            opcao = int(input('Digite a opção desejada: '))

            if opcao in menu_opcao:
                opcao_selecionada = menu_opcao[opcao]

                if opcao_selecionada == saque:
                    if saques_realizados_hoje >= LIMITE_SAQUE:
                        print('Limite de saques diários excedido.')
                        print('Saque não realizado.')
                        print('Tente novamente amanhã.')
                    else:
                        saldo, saque_valor = opcao_selecionada(saldo)
                        if saque_valor is not None:
                            transacoes.append(f"Saque: R${saque_valor:.2f}")
                            saques_realizados_hoje += 1

                elif opcao_selecionada == deposito:
                    saldo, deposito_valor = opcao_selecionada(saldo)
                    if deposito_valor is not None:
                        transacoes.append(f"Depósito: R${deposito_valor:.2f}")
                elif opcao_selecionada == extrato:
                    opcao_selecionada(saldo, transacoes)
                elif opcao_selecionada == sair:
                    opcao_selecionada()
                    break
                else:
                    opcao_selecionada()

            else:
                print('Opção inválida')
                print('Tente novamente')

        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')

movimentacao()