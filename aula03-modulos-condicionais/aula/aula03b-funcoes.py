# FUNCOES
#==========================================
def print_lyrics():
    print("E foi chocante ver você de novo na minha frente")
    print("E o impacto de não ser tão diferente")

print_lyrics()              # exibe o conteudo
print(print_lyrics)         # exibe o local que a funcao esta
print(type(print_lyrics))

print()

def saudar_usuario(nome):
    return f"Olá, {nome}! Bem-vinda ao curso"

mensagem = saudar_usuario(input('Digite seu nome: '))
print(mensagem)

escola = "FIAP" # GLOBAL (visível em qualquer lugar)

def minha_aula():
    materia = "Python" # LOCAL (só existe aqui dentro)
    print(f"Estudando {materia} na {escola}")

minha_aula()
