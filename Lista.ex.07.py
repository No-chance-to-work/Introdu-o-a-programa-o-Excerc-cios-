altura_thanos = 150
altura_aranha = 110

crescimento_thanos = 2
crescimento_aranha = 3

for i in range(1000):
    altura_thanos += crescimento_thanos
    altura_aranha += crescimento_aranha
    
    if altura_aranha > altura_thanos:
        print(f"Serão necessários {i + 1} anos para que o Homem-Aranha seja maior que Thanos.")
        break
else:
    print("O Homem-Aranha nunca será maior que Thanos.")