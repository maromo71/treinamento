usuarios = [
    {"nome": "Ana", "idade": 21},
    {"nome": "Pedro", "idade": 14},
    {"nome": "Zeca", "idade": 70}
]
print(usuarios)

for usuario in usuarios:
    print(f'Nome: {usuario["nome"]} sua idade: {usuario["idade"]}')


escoteiros = {
    "Maromo": 21,
    "Pedro": 11,
    "Antonio": 15
}
for chave in escoteiros.keys():
    print(f'{chave} tem {escoteiros[chave]} anos')