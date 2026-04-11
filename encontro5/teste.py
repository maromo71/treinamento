nomes = input("Digite os nomes separados por virgula")
novo = [nome.strip() for nome in nomes.split(",")]
print(novo)