contnegativo=0
somavalor=0
for i in range(20):
    valor=int(input("Digite o valor: "))
    if valor>=0:
       somavalor+=valor
    else:
       contnegativo+=1
print("A soma dos valores positivos é:", somavalor)
print("A quantidade de valores negativos é:",contnegativo)