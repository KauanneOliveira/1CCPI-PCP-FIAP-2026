# === DESAFIO 1 ===
print("\n--- SITUAÇÃO DO VOTO ELEITORAL ---")

idade = int(input('Digite o numero da sua idade: '))

if (idade >= 16 and idade < 18) or (idade > 70):
    print("Voto é opcional!")
elif idade < 16:
    print("Voto não é permitido para menores de 16 anos")
else:
    print("Voto é obrigatório!")
