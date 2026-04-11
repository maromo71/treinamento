import collections as deque

def criar_fila():
    # retorna uma nova fila (fila vazia)
    return deque.deque()

def inserir_fila(fila, elemento):
    # insere um elemento no final da fila
    fila.append(elemento)

def remover_fila(fila):
    #remover o primeiro elemento da fila
    if not fila:
        raise IndexError("Impossível Remover em lista vazia")
    else:
        return fila.popleft()
    
def visualizar_proximo(fila):
    # espiar o primeiro elemento da fila
    if not fila:
        raise IndexError("Fila vazia, nao podemos visualizar proximo")
    else:
        return fila[0]

def exibir_fila(fila):
    # devolve a fila para percorrer
    return list(fila)

def esta_vazia(fila):
    # se for vazia retorna true, caso contrario false
    return len(fila) == 0

def tamanho(fila):
    # retorna o numero de elementos na fila
    return len(fila)

def construir_menu():
    # menu de iteração com o usuario
    print("=" * 60)
    print("1. Inserir cliente na fila")
    print("2. Remover cliente da fila")
    print("3. Visualizar proximo a ser atendido")
    print("4. Verificar se a fila está vazia")
    print("5. Obter tamanho da fila")
    print("6. Exibir a fila")
    print("9. SAIR do programa")

def main():
    # gerenciar a fila de clientes de um banco, sem prioridade
    fila = criar_fila()
    while True:
        print("\nMENU")
        construir_menu()
        escolha = input("Escolha uma opcao: ")
        print("=" * 60)
        if escolha == "1":
            cliente = input("Digite o nome do cliente: ")
            inserir_fila(fila, cliente)
            print(f"Cliente entrou na fila: {cliente}")
        elif escolha == "2":
            try:
                cliente = remover_fila(fila)
                print(f"Cliente a ser atendido no momento {cliente}")
            except IndexError as erro:
                print(erro)
        elif escolha == "3":
            try:
                cliente = visualizar_proximo(fila)
                print(f"Próximo cliente na fila {cliente}")
            except IndexError as erro:
                print(erro)
        elif escolha == "4":
            vazia = esta_vazia(fila)
            if vazia:
                print("Não há clientes na fila")
            else:
                print("Há clientes para ser(em) atendido(s)")
        elif escolha == "5":
            tam = tamanho(fila)
            print(f"Tamanho da fila: {tam}")
        elif escolha == "6":
            clientes = exibir_fila(fila)
            print("Ordem para atendimento")
            for cliente in clientes:
                print(f"Cliente: {cliente}")
        elif escolha == "9":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()