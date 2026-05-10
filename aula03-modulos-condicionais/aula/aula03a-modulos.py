# MODULOS
#==========================================

# modulo para usar funcoes matematicas
import math

# raiz quadrada de um numero
numero = 25
raiz = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz:.2f}")

# seno de 45 graus
graus = 45
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print(seno)

# numeros aleatorios
import random

# gera num aleatorio entre 0 e 1
# num aleatorio entre 0 e 10
num_random = random.random()
print (num_random * 10)

# num int de 1 a 10
num_random_int = random.randint(1, 10)
print(num_random_int)