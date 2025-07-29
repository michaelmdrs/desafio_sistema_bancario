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

        else:
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