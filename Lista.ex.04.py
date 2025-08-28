soma_alturas = 0
NumJogadores = int(input("Digite o numero de jogadores:"))
if NumJogadores <=0:
    print("O numero de jogadores é invalido.")
else:
    print("O numero de jogadores é valido.")
    for i in range(1, NumJogadores + 1):
      altura = float(input(f"Digite a altura do jogador {i}: "))
      soma_alturas += altura
    altura_media = soma_alturas / NumJogadores
    print("A altura media dos jogadores é:", altura_media ,)