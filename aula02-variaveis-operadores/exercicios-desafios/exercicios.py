# === EXER 1 ===
print("--- CALCULO DA AREA DE UM CIRCULO ---")

raio = 5
area = 3.141519 * raio**2;

print(f"Valor do raio: {raio}")
print(f'A area do circulo e: {area:.2f}')
print()

# === EXER 2 ===
print("--- CONVERSOR DE TEMPERATURA ---")
print("\tFahrenheit para Celsius")

temp_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
temp_celsius = (temp_fahrenheit - 32) * 5 / 9

print(f'{temp_fahrenheit:.1f} em Fahrenheit = {temp_celsius:.1f} em Celsius')
print()


# === EXER 3 ===
print("--- CONVERSOR DE TEMPERATURA ---")
print("\tCelsius para Fahrenheit")


temp_celsius = float(input('Digite a temperatura em Celsius: '))
temp_fahrenheit = (temp_celsius * 9 / 5) + 32

print(f'{temp_celsius:.1f} em Fahrenheit = {temp_fahrenheit:.1f} em Celsius')
print()

# === EXER 4 ===
print("--- CALCULADORA DE GASTO ---")
print("3- livros por 25 reais cada\n2- canetas por 5 reais cada")

livro = 25
caneta = 5
print(f'Gasto total: {(3 * livro) + (2 * caneta)}')
print()

# === EXER 5 ===
print("--- CALCULADORA DE TEMPO---")

'''Um carro percorreu 150 km a uma velocidade média de 60 km/h. Quanto tempo (em horas) o carro levou para percorrer essa distancia?')'''

distancia = 150
velocidade_media = 60
tempo = distancia / velocidade_media

print(f"O tempo foi de: {tempo} horas")
print()


# === EXER 6 ===
print("--- MEDIA DE DUAS NOTAS ---")


A = float(input("Digite a primeira nota: "))
B = float(input("Digite a segunda nota: "))
print(f'\nA media do aluno e: {(A + B) / 2}')
print()

# === EXER 7 ===
print("--- MEDIA DE NOTAS COM PESO DIFERENTES---")

A = float(input("Digite a primeira nota: "))
B = float(input("Digite a segunda nota: "))
media = ((A * 4) + (B * 6)) / 10
print(f'\nA media do aluno e: {media}')
print()


# === EXER 8 ===
print("--- GASTO TOTAL (PECAS) ---")

peca1 = input('Digite o nome da primeira peca: ')
qtd_peca1 = int(input('Digite a quantidade que deseja: '))
valor_peca1 = float(input('Digite o valor da primeira peca: '))

peca2 = input('\nDigite o nome da segunda peca: ')
qtd_peca2 = int(input('Digite a quantidade que deseja: '))
valor_peca2 = float(input('Digite o valor da segunda  peca: '))

total_peca1 = (qtd_peca1 * valor_peca1)
total_peca2 = (qtd_peca2 * valor_peca2)

print(f"\nValor total da(o) {peca1}: {total_peca1}")
print(f"Valor total da(o) {peca2}: {total_peca2}")
print(f'Valor final a ser pago pelas pecas: {total_peca1 + total_peca2}')
print()


# === EXER 9 ===
print("--- TROCO DE PAGAMENTO ---")

valor_produto = float(input('Digite o valor do produto: '))
valor_pago = float(input('Digite o valor do pagamento: '))

troco = valor_pago - valor_produto

print(f"O valor do troco do cliente e: `{troco}")
