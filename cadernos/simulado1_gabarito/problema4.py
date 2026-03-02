def resolver():
   N = int(input())
   if N > 1 and N < 1000:
    # O loop vai de 1 até N (inclusive)
    for i in range(1, N + 1):
        # Primeira linha: i, i^2, i^3
        quad = i * i
        cubo = i * i * i
        print(f"{i} {quad} {cubo}")
        # Segunda linha: i, i^2+1, i^3+1
        print(f"{i} {quad + 1} {cubo + 1}")

def main():
    resolver()

if __name__ == "__main__":
    main()