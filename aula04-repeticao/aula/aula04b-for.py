for count_music in range(3):
     print(f"Música {count_music}")

print()

# de 1 até 11, pulando de 2 em 2
for i in range(1, 12, 2):
    print(i)

print()

# ATV. 3
qtd_musicas = int(input("Digite a qtd de musicas que vc tem na playlist (DB): "))

for i in range(qtd_musicas):
    print(f"Música {i}")

print()

# correndo em linhas e colunas (array)
# 5 linhas, 4 colunas, incrementa 2
# acessa apenas a coluna 0 e 2
for i in range(0, 4):
    for j in range(0, 3, 2):
        print(f"i:{i}, j:{j}")