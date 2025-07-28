class Pessoa():
    def __init__(self, nome, cpf_cnpj):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf_cnpj}"


class Cliente(Pessoa):
    def __init__(self, nome, cpf_cnpj, endereco, contas=None):
        super().__init__(nome, str(cpf_cnpj))
        self.endereco = endereco
        self.contas = contas if contas is not None else []


    def get_tipo_documento(self):
        documento_limpo = ''.join(filter(str.isdigit, self.cpf_cnpj))

        if len(documento_limpo) == 11:
            return 'CPF'
        elif len(documento_limpo) == 14:
            return 'CNPJ'
        else:
            return 'Documento inválido'

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta():
    def __init__(self, numero, agencia, saldo_inicial=0):
        self.numero = numero
        self.agencia = agencia
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado. \nNovo saldo R$: {self._saldo}')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor <= 0:
            print('Valor de saque inválido.')
        elif valor > self._saldo:
            print('Saldo insuficiente')
        else:
            self._saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado. \nNovo saldo R$: {self._saldo}')

    def __str__(self):
        return f"Conta: {self.numero}, Agência: {self.agencia}, Saldo: R$ {self.saldo:.2f}"

    


cliente_maria = Cliente('Maria', '12345678910', 'Rua Sem Nome')
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