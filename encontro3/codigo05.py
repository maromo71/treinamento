# gerar um numero aleatorio entre 1 e 1000
import random
magico = random.randint(1, 1000)
contador = 1
while True:
    if contador == 11:
        print("Pena, voce perdeu. O numero magico: ", magico)
        break
    print("Tentativa: ", contador)
    chute = int(input("Digite o seu palpite: "))
    contador += 1
    if chute == magico:
        print("Parabens!! pegue a grana")
        break
    elif chute < magico:
        print("Chute Baixo...")
        continue
    else:
        print("Chute Alto...")
        continue