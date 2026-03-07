a = {5, 3, 7}
b = {9, 7, 11}

unidos = a.union(b)
print(unidos)

interseccao = a.intersection(b)
print(interseccao)

diferenca = a.difference(b)
print(diferenca)

diferenca = b.difference(a)
print(diferenca)

simetrica = a.symmetric_difference(b)
print(simetrica)
