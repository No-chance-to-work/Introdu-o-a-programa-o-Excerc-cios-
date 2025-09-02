numero = int(input("Digite um número inteiro não negativo: "))

if numero < 0:
    print("Fatorial não definido para números negativos.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")