def resolver():
    # entrada linha a linha
    num = int(input())
    horas = int(input())
    valor = float(input())
    salario = horas * valor
    print(f"NUMBER = {num}")
    print(f"SALARY = U$ {salario:.2f}")

def main():
    resolver()

if __name__ == "__main__":
    main()