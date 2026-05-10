"""
# === EXER 1 ===
import os

print("--- REPRODUZINDO ÁUDIO ---")

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
    print("Reprovado") """

# === EXER 4 ===
print("\n--- MEDIA DE 4 NOTAS ---")