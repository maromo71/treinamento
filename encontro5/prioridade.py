import heapq
import time
import os
import itertools

# Gerador para manter a ordem de chegada (desempate para a mesma prioridade)
contador = itertools.count()

def adicionar_cliente(nome, prioridade, fila_cliente):
    """
    Simula uma fila de cliente do banco com prioridade.
    Prioridade 1: Preferencial (Alta)
    Prioridade 2: Normal (Baixa)
    """
    if fila_cliente is None:
        fila_cliente = []
        
    # Obtém o próximo número inteiro da sequência de chegada
    ordem_chegada = next(contador)
    
    # O heapq organiza os elementos com base no primeiro item da tupla (prioridade).
    # Em caso de empate na prioridade, ele usa o segundo item (ordem_chegada) para manter o FIFO.
    cliente = (prioridade, ordem_chegada, nome)
    heapq.heappush(fila_cliente, cliente)
    
    tipo_cliente = "Preferencial" if prioridade == 1 else "Normal"
    print(f"Adicionando cliente {nome} ({tipo_cliente})")
    
    # Para exibir, ordenamos a fila e pegamos apenas os nomes
    nomes_na_fila = [c[2] for c in sorted(fila_cliente)]
    print(f"\nFila de Clientes (Ordenada): {nomes_na_fila}")
    print("=" * 60)
    return fila_cliente

def chamar_atendimento(fila_cliente):
    """
    Função que remove e devolve o cliente com maior prioridade.
    """
    if fila_cliente:
        # heappop sempre remove o menor elemento (ou seja, prioridade 1 antes da 2)
        prioridade, ordem, nome = heapq.heappop(fila_cliente)
        tipo = "Preferencial" if prioridade == 1 else "Normal"
        
        print(f"Cliente {nome} ({tipo}) sendo atendido no caixa...")
        time.sleep(1)
        
        nomes_na_fila = [c[2] for c in sorted(fila_cliente)]
        print(f"Fila atual: {nomes_na_fila}")
    else:
        print("Não há clientes na fila no momento.")

def mostrar_proximo(fila_cliente):
    if fila_cliente:
        # Em um heap, o índice 0 sempre é o menor elemento absoluto
        proximo = fila_cliente[0]
        tipo = "Preferencial" if proximo[0] == 1 else "Normal"
        print(f"O próximo a ser atendido é: {proximo[2]} ({tipo})")
    else:
        print("Não há ninguém mais a ser atendido.")

def main():
    fila_cliente = []
    while True:
        time.sleep(2)
        # Limpa a tela de forma compatível com Windows (nt) ou Linux/Mac (posix)
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("=" * 60)
        print("\nFILA DO BANCO - ATENDIMENTO COM PRIORIDADE")
        print("1. Cliente Normal entra na fila")
        print("2. Cliente Preferencial entra na fila")
        print("3. Atender um cliente")
        print("4. Mostra o próximo cliente")
        print("5. Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente normal: ")
            fila_cliente = adicionar_cliente(nome, 2, fila_cliente)
        elif opcao == "2":
            nome = input("Digite o nome do cliente preferencial (Idoso/Gestante): ")
            fila_cliente = adicionar_cliente(nome, 1, fila_cliente)
        elif opcao == "3":
            chamar_atendimento(fila_cliente)
        elif opcao == "4":
            mostrar_proximo(fila_cliente)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()