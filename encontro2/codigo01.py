ativo = True
acabado = False

print(ativo)
print(acabado)

nome = "Oscar"
print(nome)

nome = "Zelia da Silva"
print(nome)
print(nome[0])
print(nome[2:7])
print(nome.upper())
print(nome.lower())
nome = nome.replace("Silva", "Souza")
print(nome)
exemplo = "       ola turma        "
print(exemplo.strip())
frase = "Fui pescar ontem, estava escuro"
fatia = frase.split(" ")
print(fatia)
texto = "Antonio Carlos Santos;23.90;Abril"
vetor = texto.split(";")
print(vetor[0])
print(len(vetor[0])) # tamanho do nome (21 caracteres)