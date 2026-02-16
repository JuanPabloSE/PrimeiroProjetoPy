print("---- MÉDIA NOTA FINAL ----")
print()

nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

print(f"\nMédia final: {media:.2f}")

# Estrutura condicional
if media >= 7.0:
    print(f"Parabéns {nome}, você foi APROVADO!")
elif media >= 5.0:
    print(f"{nome}, você está na RECUPERAÇÃO!")
else:
    print(f"{nome}, você infelizmente foi REPROVADO!")
