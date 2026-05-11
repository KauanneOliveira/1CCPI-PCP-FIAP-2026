"""
Em muitos dos nossos algoritmos fizemos validações dos dados de entrada. Contudo, apenas exibíamos mensagens e encerrávamos nossos algoritmos. Com os comandos de repetição temos condições de garantir que a informação esteja correta antes do algoritmo continuar.
▪ Atividade 2: Escreva um programa que dadas duas notas de 0 a 10 calcula a média aritmética entre elas
"""

def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite novamente a nota: "))
    return nota

notaA = float(input("Digite a 1ª nota: "))
notaA = validar_nota(notaA)

notaB = float(input("Digite a 2ª nota: "))
while notaB < 0 or notaB > 10:
    print("A nota deve estar entre 0 e 10")
    notaB = float(input("Digite novamente a nota: "))

media = (notaA + notaB) / 2
print(f"Média: {media}")
