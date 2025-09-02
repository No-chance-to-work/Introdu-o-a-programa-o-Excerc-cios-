alunos = 10
medias = []
aprovados = 0
reprovados = 0

for i in range(1, alunos + 1):
    print(f"\nAluno {i}:")
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    
    media = (n1 + n2 + n3) / 3
    medias.append(media)

    print(f"Média do aluno {i}: {media:.2f}")

    if media >= 6:
        aprovados += 1
    else:
        reprovados += 1

maior_media = max(medias)
menor_media = min(medias)

print("\n--- Resultados ---")
print(f"Maior média: {maior_media:.2f}")
print(f"Menor média: {menor_media:.2f}")
print(f"Total de aprovados: {aprovados}")
print(f"Total de reprovados: {reprovados}")