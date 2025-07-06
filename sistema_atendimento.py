def ordenar_pacientes(pacientes):
    def ordenar_por_prioridade(paciente):
        nome, idade, status = paciente
        prioridade_status = 2
        if status.lower() == "urgente":
            prioridade_status = 0
        elif idade > 60:
            prioridade_status = 1
        return (prioridade_status, -idade)
    return sorted(pacientes, key=ordenar_por_prioridade)


qtd_pacientes = int(input("Digite a quantidade de pacientes: "))

pacientes = []
for i in range(qtd_pacientes):
    nome, idade, status = input('Digite o nome, idade e status do paciente (separados por vírgula): ').strip().split(', ')
    idade = int(idade)
    pacientes.append((nome, idade, status))
    if idade > 60:
        print(f'{nome} é um paciente idoso e deve ser atendido com prioridade.')
    elif status.lower() == 'urgente':
        print(f'{nome} é um paciente com status urgente e deve ser atendido imediatamente.')
    else:
        print(f'{nome} é um paciente com status normal e pode aguardar atendimento.')

print("\n--- Ordem de Atendimento Prioritária ---")
pacientes_ordenados = ordenar_pacientes(pacientes)
pacientes_ordenados = [paciente[0] for paciente in pacientes_ordenados]
lista_de_atendimentos = ', '.join(pacientes_ordenados)
print(f"Ordem de atendimentos: {lista_de_atendimentos}")
