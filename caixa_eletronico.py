# Sistema Bancário - Caixa Eletrônico V2.0
import datetime, time, textwrap
from abc import ABC, abstractclassmethod, abstractproperty

usuarios = []
conta = []
numero_conta = 1

class ContaIterador:
    def __init__(self, contas):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


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
    menu = 'CADASTRO [1] | CRIAR CONTA [2] | SAQUE [3] | DEPÓSITO [4] | EXTRATO [5] | SAIR [6]'
    print(menu.center(65).upper())
    print(65 * '=')


def log_transacoes(func):
    def wrapper(*args, **kwargs):
        hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        resultado = func(*args, **kwargs)
        print(f'\n[LOG] Transação: {func.__name__.upper()} | Data e Hora: {hora}')
        return resultado
    return wrapper


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


@log_transacoes
def saque(saldo):
    valor = float(input('Digite o valor do saque: '))
    if valor <= 0:
        print('Valor inválido. Saque não realizado.')
        return saldo, None
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
def cria_conta(contas, usuarios, numero_conta):
    print("Bem-vindo ao ONBANK ONLINE!")
    print("Para criar uma conta, por favor, preencha as informações solicitadas.")
    cpf = input('Digite seu CPF: ').strip()
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if not usuario:
        print('Usuário não encontrado. Por favor, cadastre-se primeiro.')
        return numero_conta
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(conta)
    print('Conta criada com sucesso!')
    print(f'Agência: {conta["agencia"]}')
    print(f'Número da Conta: {numero_conta}')
    print(f'Titular: {usuario["nome"]}')
    return numero_conta + 1

@log_transacoes
def cadastrar_usuario():
    nome = input('Digite seu nome: ').strip().title()
    cpf = input('Digite seu CPF: ').strip()
    data_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ').strip()
    if not nome or not cpf or not data_nascimento:
        print('Todos os campos são obrigatórios. Cadastro não realizado.')
        return
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print('Usuário já cadastrado com este CPF.')
            return
    usuarios.append({
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento
    })
    print(f'Usuário {nome} cadastrado com sucesso!')

@log_transacoes
def sair():
    sleep(2)
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
    1: cadastrar_usuario,
    2: cria_conta,
    3: saque,
    4: deposito,
    5: extrato,
    6: sair
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
            elif opcao_selecionada == cadastrar_usuario:
                cadastrar_usuario()
            elif opcao_selecionada == cria_conta:
                numero_conta = cria_conta(conta, usuarios, numero_conta)
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


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
        })

    def gerar_relatorio(self, tipo_transacao=None):
        pass


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
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor