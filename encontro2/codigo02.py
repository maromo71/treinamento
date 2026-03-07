# vetor em Python ===> lista
valores = [1, 5, 7, 9, 11]
# print(valores[3:5]) # saida 9 e 11.Primeiro inclusive, ultimo: exclusive
# print(valores[3])

lista = [32, 1, 7, 8, 0, 21]
print(lista)
lista.append(14)
print(lista)

for i in range(10):
    lista.append(int(input("Digite um valor: ")))

print(lista)
print(len(lista))


