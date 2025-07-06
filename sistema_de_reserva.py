def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input('Digite os números dos quartos disponíveis (separados por espaço): ').split()))
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input('Digite os números dos quartos solicitados (separados por espaço): ').split()))
    print(f'DEBUG: reservas_solicitadas: {reservas_solicitadas}')
    # TODO: Crie o processamento das reservas:
    confirmadas = []
    recusadas = []
    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos:
    for quarto_solicitado in reservas_solicitadas:
        if quarto_solicitado in quartos_disponiveis:
            confirmadas.append(quarto_solicitado)
            quartos_disponiveis.remove(quarto_solicitado)
        else:
            recusadas.append(quarto_solicitado)
    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal


processar_reservas()
