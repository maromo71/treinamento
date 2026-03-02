
import math # para encontrar a raiz de dekta

def resolver():
    # Leitura dos três valores de ponto flutuante na mesma linha
    linha = input().split() # ler a linha como um vetor
    A = float(linha[0])
    B = float(linha[1])
    C = float(linha[2])

    # Cálculo do Delta (B^2 - 4AC)
    delta = (B ** 2) - (4 * A * C)

    # Verificação das condições de impossibilidade:
    # 1. A não pode ser 0 (divisão por zero)
    # 2. Delta não pode ser negativo (raiz quadrada de número negativo)
    if A == 0 or delta < 0:
        print("Impossivel calcular")
    else:
        # Cálculo das duas raízes usando a função math.sqrt para a raiz quadrada
        r1 = (-B + math.sqrt(delta)) / (2 * A)
        r2 = (-B - math.sqrt(delta)) / (2 * A)

        # Impressão dos resultados com 5 casas decimais
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")

def main():
    # invocar a funcao para resolver
    resolver()

if __name__ == "__main__":
    main()