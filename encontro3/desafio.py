def soma_leds(valor):
    soma = 0
    for c in str(valor):
        soma += lista_leds[int(c)]
    return soma

lista_leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

N = int(input())
if not (1 <= N <= 1000):
    exit()

V = []
for i in range(N):
    valor = int(input())
    if not (1 <= valor <= 10100):
        exit
    V.append(valor)

# calcular o numero de leds por valor
for i in range(N):
    res = soma_leds(V[i])
    print(res, "leds")
