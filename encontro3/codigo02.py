def main():
    salario = float(input())

    if salario < 2500:
        novo_salario = salario * 1.10
    elif salario < 3700:
        novo_salario = salario * 1.09
    else:
        novo_salario = salario * 1.08

    print("{:.2f}".format(novo_salario))

if __name__ == "__main__":
    main()

