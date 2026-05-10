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

tempFahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
tempCelsius = (tempFahrenheit - 32) * 5 / 9

print(f'{tempFahrenheit:.1f} em Fahrenheit = {tempCelsius:.1f} em Celsius')
print()


# === EXER 3 ===
print("--- CONVERSOR DE TEMPERATURA ---")
print("\tCelsius para Fahrenheit")


tempCelsius = float(input('Digite a temperatura em Celsius: '))
tempFahrenheit = (tempCelsius * 9 / 5) + 32

print(f'{tempCelsius:.1f} em Fahrenheit = {tempFahrenheit:.1f} em Celsius')
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
velocidadeMedia = 60
tempo = distancia / velocidadeMedia

print(f"O tempo foi de: {tempo} horas")
print()


# === EXER 6 ===
print("--- MEDIA DE DUAS NOTAS ---")

'''Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
aritmética do aluno'''

A = float(input("Digite a primeira nota: "))
B = float(input("Digite a segunda nota: "))
print(f'\nA media do aluno e: {(A + B) / 2}')
print()

# === EXER 7 ===
print("--- MEDIA DE NOTAS COM PESO DIFERENTES---")

'''Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule e informe a média
ponderada do aluno, sabendo que a nota A tem peso 4 e a nota B tem peso 6.'''

A = float(input("Digite a primeira nota: "))
B = float(input("Digite a segunda nota: "))
media = ((A * 4) + (B * 6)) / 10
print(f'\nA media do aluno e: {media}')
print()


# === EXER 8 ===
print("--- GASTO TOTAL (PECAS) ---")

'''Neste problema, deve-se ler o nome de uma peça que chamaremos de peça1, o número de peças1 que
o usuário quer, o valor unitário de cada peça1, o nome de uma peça2, o número de peças2 e o valor
unitário de cada peça2. Após, calcule e mostre o valor a ser pago'''

peca1 = input('Digite o nome da primeira peca: ')
qtdPeca1 = int(input('Digite a quantidade que deseja: '))
valorPeca1 = float(input('Digite o valor da primeira peca: '))

peca2 = input('\nDigite o nome da segunda peca: ')
qtdPeca2 = int(input('Digite a quantidade que deseja: '))
valorPeca2 = float(input('Digite o valor da segunda  peca: '))

totalPeca1 = (qtdPeca1 * valorPeca1)
totalPeca2 = (qtdPeca2 * valorPeca2)

print(f"\nValor total da(o) {peca1}: {totalPeca1}")
print(f"Valor total da(o) {peca2}: {totalPeca2}")
print(f'Valor final a ser pago pelas pecas: {totalPeca1 + totalPeca2}')
print()


# === EXER 9 ===
print("--- TROCO DE PAGAMENTO ---")

'''
▪ Crie um programa que receba o valor do produto e valor pago.
▪ Calcule o troco a ser pago. 
▪ O valor do troco deve ser exibido no terminal
'''

valorProduto = float(input('Digite o valor do produto: '))
valorPago = float(input('Digite o valor do pagamento: '))

troco = valorPago - valorProduto

print(f"O valor do troco do cliente e: `{troco}")
