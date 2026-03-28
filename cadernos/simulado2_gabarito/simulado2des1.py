import sys

def resolver_desafio():
    # comum em maratonas usar sys.stdin para velocidade
    try:
        entrada = input().strip()
    except EOFError:
        return

    pilha = []

    for char in entrada:
        if char == '#':
            # Operação LIFO: Remove se houver algo para remover
            if pilha:
                pilha.pop()
        else:
            # Operação LIFO: Adiciona o caractere no topo
            pilha.append(char)

    # Transformando a pilha de volta em string para exibição
    resultado = "".join(pilha)
    print(resultado)

# Execução do script
if __name__ == "__main__":
    resolver_desafio()

