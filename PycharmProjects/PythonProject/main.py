""""
===============================



===================================




num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
operacao = input('Digite o simbolo de uma das operações matematicas (+, -, *, /) : ')

match operacao:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        print(num1 / num2)
    case _:
        print('Digite uma operacao valida!')

def saudar_usuario(nome):
    return f"Olá, {nome}! Bem-vinda ao curso"

mensagem = saudar_usuario(input('Digite seu nome: '))
print(mensagem)

escola = "FIAP" # GLOBAL (visível em qualquer lugar)

def minha_aula():
    materia = "Python" # LOCAL (só existe aqui dentro)
    print(f"Estudando {materia} na {escola}")

minha_aula()

cp = 0
while cp < 10:
    cp += 1

    if cp == 3:
        continue

    print(f"Produuto {cp}")


# Ativ 2:

nota1 = -1
nota2 = -1

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Digite a primeira nota (0 a 10): "))
    if nota1 < 0 or nota1 > 10:
        print("Nota inválida! Digite um valor entre 0 e 10.")

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Digite a segunda nota (0 a 10): "))
    if nota2 < 0 or nota2 > 10:
        print("Nota inválida! Digite um valor entre 0 e 10.")

media = (nota1 + nota2) / 2
print(f"Média final: {media}")

for cp in range(3):
    print('Produto')

qtdProdutos = int(input('Digite a quantidade de produtos: '))
for cp in range(qtdProdutos):
    print('Produto') """

continua = 's'

while continua == 's':
    print('Olá, Mundo')
    continua = input('Deseja continuar? - [s]im, [n]ao: ')

print('Fim')
