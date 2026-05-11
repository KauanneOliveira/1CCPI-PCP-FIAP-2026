# === EXER 1 ===
print("--- MENSAGEM EM LOOP ---")

resposta = 's'

while resposta.lower() != 'n':
    print('\tOlá Mundo');
    resposta = input('Deseja exibir a mensagem novamente? ([s]im - [n]ão): ')

# === EXER 2 ===
print("--- CONTAGEM DE 0 A 100 INCREMENTANDO 10 ---")
for i in range(0, 101, 10):
    print(i)

# === EXER 3 ===
print("--- TABUADA DE N DO 0 AO 25  ---")

num = int(input('Digite um numero inteiro que deseja a tabuada: '))

for i in range(0, 26):
    print(f'{num} X {i} = {num * i}')

# === EXER 4 ===
print("--- SOMA DE 5 VALORES ---")

soma = 0

for i in range(0, 5):
    valor = float(input(f'Digite o {i + 1}º valor: '))
    soma += valor

print(f"A soma dos valores digitados é: {soma}")

# === EXER 5 ===
print("--- O MAIOR VALOR ---")

maior_valor = 0

for i in range(0, 5):
    valor = float(input(f'Digite o {i + 1}º valor: '))

    if valor > maior_valor :
        maior_valor = valor

print(f"O maior valor digitado foi: {maior_valor}")

# === EXER 6 ===
print("--- VALORES PARES COM O LIMITE DO USUÁRIO ---")

valor = int(input(f'Digite o valor inteiro máximo do intervalo: : '))

print(f"Valores pares no intervalor de 2 a {valor}: ")

for i in range(2, valor + 1):
    if i % 2 == 0:
        print(f"{i}")

# === EXER 7 ===
print("--- SOMA DOS VALORES COM O LIMITE DO USUÁRIO ---")

valor = -1
soma = 0

while valor < 0:
    valor = int(input(f'Digite um valor inteiro positivo  máximo do intervalo: : '))

for i in range(1, valor + 1):
    soma += i

print(f"A soma de 1 até {valor}: {soma}")

# === EXER 8 ===
print("--- DIVISORES DE N ---")

valor = -1

while valor < 0:
    valor = int(input(f'Digite um valor inteiro positivo que deseja saber seus divisores: '))

for i in range(1, valor + 1):
    if valor % i == 0:
        print(i)

# === EXER 9 ===
print("--- NÚMEROS PRIMOS DE 2 A 200 ---")

for i in range(2, 201):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)
