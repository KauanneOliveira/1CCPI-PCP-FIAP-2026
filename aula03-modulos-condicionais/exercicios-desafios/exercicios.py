
# === EXER 1 ===
print("--- REPRODUZINDO ÁUDIO ---")
import os
arquivo = "musica.mp3"

# manda o sistema operacional abrir o arquivo com o player padrão
os.startfile(arquivo)

# === EXER 2 ===
print("\n--- PAR OU IMPAR ---")

num = float(input('Digite um numero: '))

if num % 2 == 0:
    print('O numero é par!')
else:
    print('O numero é ímpar!')

# === EXER 3 ===
print("\n--- MAIOR OU IGUAL ---")

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

if num1 > num2:
    print(f"O número maior é: {num1}")
elif num1 < num2:
    print(f"O número maior é: {num2}")
else:
    print("Os números são iguais!")

# === EXER 4 ===
print("\n--- MEDIA DE 4 NOTAS ---")

nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
nota3 = float(input('Digite a 3º nota: '))
nota4 = float(input('Digite a 4º nota: '))

media = (nota1 + nota2 + nota3 + nota3) / 4

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Em recuperação")
else:
    print("Reprovado")

# === EXER 5 ===
print("\n--- NUMEROS MULTIPLOS ---")

A = int(input('Digite o primeiro numero inteiro: '))
B = int(input('Digite o segundo numero inteiro: '))

if A % B == 0:
    print('São Múltiplos')
else:
    print('Não são Múltiplos')

# === EXER 6 ===
print("\n--- CALCULADORA BÁSICA ---")

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
operacao = input('Digite o simbolo de uma das operações matematicas (+, -, *, /) : ')

match operacao:
    case '+':
        print(f'Resultado: {num1 + num2}')
    case '-':
        print(f'Resultado: {num1 - num2}')
    case '*':
        print(f'Resultado: {num1 * num2}')
    case '/':
        print(f'Resultado: {num1 / num2}')
    case _:
        print('Digite uma operacao valida!')

# === EXER 7 ===
print("\n--- SITUAÇÃO DO VOTO ELEITORAL ---")

ano = int(input("Digite o ano do seu nascimento: "))
idade = 2026 - ano

if (idade >= 16 and idade < 18) or (idade > 70):
    print("O voto é opcional este ano!")
elif idade < 16:
    print("O voto é proibido este ano!")
else:
    print("O voto é obrigatório!")

# === EXER 8 ===
print("\n--- REAJUSTE SALARIAL ---")

def calcular_reajuste(salario, percentual):
    aumento = (salario * (percentual/100))
    novo_salario = salario + aumento

    print(f'Salário anterior: {salario}\n'
          f'Percentual de aumento: {percentual}%\n'
          f'Valor do aumento: {aumento}\n'
          f'Salário ajustado: {novo_salario}\n')


salario = float(input("Digite o valor do salário: "))

if salario <= 280.00:
    calcular_reajuste(salario, 20)
elif salario <= 700.00:
    calcular_reajuste(salario, 15)
elif salario <= 1500.00:
    calcular_reajuste(salario, 10)
else:
    calcular_reajuste(salario, 5)

# === EXER 9 ===
print("\n--- PROGRAMA CAMINHÃO ---")

# funcoes
def calcular_preco_carga(peso_kg, preco_unitario):
    return peso_kg * preco_unitario

def calcular_imposto(preco_carga, percentual):
    return preco_carga * percentual

def exibicoes(peso_kg, preco_carga, imposto, valor_total):
    print(f"O peso da carga em kg: {peso_kg}")
    print(f"Preço da carga: R$ {preco_carga:.2f}")
    print(f"Valor do imposto: R$ {imposto:.2f}")
    print(f"Valor total transportado: R$ {valor_total:.2f}")

# entradas
cod_estado = int(input('Digite o código do estado de origem da carga (1 a 5): '))
peso_carga_t = float(input('Digite o peso da carga em toneladas: '))
cod_carga = int(input('Digite o código da carga (10 a 40): '))


# calculos
# peso em kilos
peso_carga_kg = peso_carga_t * 1000

# preco da carga
if 10 <= cod_carga <= 20:
    preco_carga = calcular_preco_carga(peso_carga_kg, 100)
elif 21 <= cod_carga <= 30:
    preco_carga = calcular_preco_carga(peso_carga_kg, 250)
elif 31 <= cod_carga <= 40:
    preco_carga = calcular_preco_carga(peso_carga_kg, 340)

# imposto
match cod_estado:
    case 1:
        imposto = calcular_imposto(preco_carga, 0.35)
    case 2:
        imposto = calcular_imposto(preco_carga, 0.25)
    case 3:
        imposto = calcular_imposto(preco_carga, 0.15)
    case 4:
        imposto = calcular_imposto(preco_carga, 0.05)
    case 5:
        imposto = calcular_imposto(preco_carga, 0)

# valor total (carga + impostos)
valor_total = preco_carga + imposto

# exibicao
exibicoes(peso_carga_kg, preco_carga, imposto, valor_total)

# === EXER 10 ===
print("\n--- TIPOS DE TRIÂNGULO ---")


# funcoes
def ordenar_lados(a, b, c):
    if b > a:
        a, b = b, a
    if c > a:
        a, c = c, a
    if c > b:
        b, c = c, b
    return a, b, c

def classificar_triangulo(A, B, C):
    if A >= B + C:
        return "NAO FORMA TRIANGULO"

    if A ** 2 == B ** 2 + C ** 2:
        return "TRIANGULO RETANGULO"
    elif A ** 2 > B ** 2 + C ** 2:
        return "TRIANGULO OBTUSANGULO"
    else:
        return "TRIANGULO ACUTANGULO"

def classificar_lados(A, B, C):
    if A == B and B == C:
        return "TRIANGULO EQUILATERO"
    elif A == B or A == C or B == C:
        return "TRIANGULO ISOSCELES"
    else:
        return ""


a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

A, B, C = ordenar_lados(a, b, c)
tipo_triangulo = classificar_triangulo(A, B, C)
tipo_lados = classificar_lados(A, B, C)

print(f"\nLados em ordem decrescente: {A}, {B}, {C}")
print(tipo_triangulo)

if tipo_triangulo != "NAO FORMA TRIANGULO" and tipo_lados != "":
    print(tipo_lados)
