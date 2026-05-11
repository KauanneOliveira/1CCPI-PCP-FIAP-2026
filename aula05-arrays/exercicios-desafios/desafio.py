"""
Dado um conjunto de nomes de quatro pessoas, escreva um algoritmo que imprima todas as possíveis duplas que podem ser formadas.
▪ Primeiro, crie um vetor e coloque quatro nomes nele.
▪ A seguir, exiba as possíveis duplas
"""

nomes = ["Ana", "Lara", "Luiz", "Caio"]

# colocar nome + 1 evita duplas duplicadas
# pois o indice nome_seguinte sempre vai estar a frente do nome
for nome in range(len(nomes)):
    for nome_seguinte in range(nome + 1, len(nomes)):
        print(nomes[nome], nomes[nome_seguinte])