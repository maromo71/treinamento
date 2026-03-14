frase = "Ola Galera da Fatec"
print(frase)

lista = frase.split()

for palavra in lista:
    print(palavra)


outra_galera = frase.replace("Fatec", "Etec")
print(outra_galera)

maiuscula = frase.upper()
print(maiuscula)

minuscula = frase.lower()
print(minuscula)