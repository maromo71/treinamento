import sys

def inverter_string(pilha):
    invertido = []
    while(pilha):
        token = pilha.pop()
        invertido.append(token)
    return "".join(invertido).strip()


def main():
    try:
        texto = input().strip()
    except EOFError:
        sys.exit()
    
    # empilhar o texto
    pilha = []

    for token in texto:
        pilha.append(token) # push (empilhar)

    texto_invertido = inverter_string(pilha)
    print(f"Resultado final: {texto_invertido}")
    

if __name__ == "__main__":
    main()