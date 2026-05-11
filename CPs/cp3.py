print("--- MONITORAMENTO AMBIENTAL DAS SALAS ---")

temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_registro = 0
i = 0

for sala in temperaturas:
    # zerando as variaveis em cada sala para não incrementar
    soma = 0
    registro_critico = 0

    for temperatura in sala:
        soma += temperatura
        if temperatura >= 33:
            registro_critico += 1

    media = soma / 4
    i += 1

    print(f"Sala {i}\n"
          f"Média: {media}\n"
          f"Registros críticos: {registro_critico}\n")

    # comparacao para atualizar o maior registro
    if registro_critico > maior_registro:
        maior_registro = registro_critico
        sala_maior_registro = i


print(f"Sala com maior risco: Sala {sala_maior_registro}")

