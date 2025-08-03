<<<<<<< HEAD
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []


    def transacao(self, conta, transacao):
        transacao.registrar(conta)


    def adcionar_conta(self, conta):
        self.contas.append(conta)


class Pessoa(Cliente):
    def __init__(self, nome, cpf_cnpj, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf_cnpj = cpf_cnpj

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf_cnpj}, Data nascimento: {self.data_nascimento}"


class Conta():
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.cliente = cliente
        self.agencia = '0001'
        self._historico = Historico()


    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)


    @property
    def saldo(self):
        return self._saldo
    

    @property
    def numero(self):
        return self._numero


    @property
    def agencia(self):
        return self._agencia


    @property
    def cliente(self):
        return self._cliente


    @property
    def historico(self):
        return self._historico


    def sacar(self, valor):
        saldo - self.valor
        excede_o_saldo = valor > saldo

        if excede_o_saldo:
            print('\n@@@ Operação inválida! Saldo insuficiente. @@@')
        elif valor <= 0:
            print('Valor de saque inválido.')
        elif valor > 0:
            self._saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado. \nNovo saldo R$: {self._saldo}')
            return True
        else:
            print('\n@@@ Operação inexistente. Tente novamente!')

        return False


    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado. \nNovo saldo R$: {self._saldo}')
=======
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

>>>>>>> d7ef435 (feature: implementando decoradores para gerar log das transações como data e hora.)

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
<<<<<<< HEAD
            print('Valor de depósito inválido.')
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque


    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacao if transacao['tipo'] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque

        if excedeu_limite:
            print('\n@@@ Operação inválida! O valor do saque excede o limite. @@@')

        elif excedeu_saques:
            print('\n@@@ Operação inválida! Número máximo de saques excedidos. @@@')

        else:
            return super().sacar(valor)

        return False


def __str__(self):
    return f"""\n
        Agência: \t{self.agencia}
        C/C: \t\t{self.numero}
        Titular: \t{self.cliente.nome}
    """


class Historico:
    def __init__(self):
        self.transacoes = []


    @property
    def transacoes(self):
        return self.transacoes


    def adicionar_transacao(self, transacao):
        self.transacoes.append({
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime('%d-%m-%Y %H:%S')
            })


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass


    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor


    @property
    def valor(self):
        return self.valor


    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

        else:
            print('Não há histórico de movimentação.')


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor


    @property
    def valor(self):
        return self._valor


    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

        else:
            print('Não há histórico de movimentação.')


conta_maria_corrente = Conta('0001-5', '001', 1500)
conta_maria_poupanca = Conta('0002-3', '001', 500)

cliente_maria.adicionar_conta(conta_maria_corrente)
cliente_maria.adicionar_conta(conta_maria_poupanca)

print(f'Cliente cadastrado: {cliente_maria.nome}, CPF/CNPJ: {cliente_maria.cpf_cnpj}')
print(f'Tipo de documento: {cliente_maria.get_tipo_documento()}')

print(f'\nContas de {cliente_maria.nome}')

for conta in cliente_maria.contas:
    print(conta)

print('=' * 60)
=======
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
>>>>>>> d7ef435 (feature: implementando decoradores para gerar log das transações como data e hora.)
