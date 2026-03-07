lista = [21, 11, 11, 11, 23, 45, 66, 66, 7]

# linha abaixo, remove os elementos repetidos (set - conjunto)
# em seguida transformo em lista novamente, atribuindo à mesma
# variável
lista = list(set(lista)) 
lista.sort()
print(lista)