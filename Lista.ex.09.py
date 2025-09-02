numero = int(input("Digite um número inteiro maior que 1: "))

if numero <= 1:
    print("Números menores ou iguais a 1 não são primos.")
else:
    e_primo = True

    for i in range(2, numero):
        if numero % i == 0:
            e_primo = False 
        else:
            continue 

    if e_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")