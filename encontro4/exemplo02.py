
import sys

def cifrador_fatec(frase):
    return " ".join(palavra[::-1] for palavra in frase.split())
'''
    pilha = []
    result = []
    # adicionar um espaco no final para processar a ultima palavra
    frase += " "
    # passar por cada caracter da frase
    for c in frase:
        if c != " ":
            # se nao eh um espaco, empilha a letra na pilha
            pilha.append(c)
        else:
            # se achou um espaco, esvazia a pilha no result
            while pilha:
                result.append(pilha.pop())
            result.append(" ")
    # retorna a lista de caracteres como uma string unica 
    return "".join(result).strip()
'''

def main():
    try:
        frase = input().strip()
    except EOFError:
        sys.exit()

    cifrada = cifrador_fatec(frase)

    print(f"Texto Original: {frase}")
    print(f"Texto Cifrado: {cifrada}")

if __name__ == "__main__":
    main()