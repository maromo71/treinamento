def resolver():
    # entrada de um numero
    N = int(input())
    # o maior cuidado aqui é imprimir onde tem espacos
    # com espacos, e quando nao tem, nao imprimir os espacos
    if N > 5 and N < 2000:
        for i in range(2, N + 1, 2):
            print(f"{i}^{i} =", i**i)
    else:
        exit()

def main():
    resolver()

if __name__ == "__main__":
    main()