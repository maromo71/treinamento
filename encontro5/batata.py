import collections
import time
import os

def batata_quente(nomes, num_passes):
    """
    Simula o jogo da Batata Quente usando uma Fila (Queue - FIFO).
    Demonstra a técnica de rotacionar uma fila.
    """
    # Cria a fila usando deque para operações O(1) nas extremidades
    fila = collections.deque(nomes)
    
    print("\n" + "=" * 50)
    print(" 🔥 INICIANDO O JOGO DA BATATA QUENTE 🔥 ")
    print("=" * 50)
    print(f"Roda inicial: {list(fila)}\n")
    
    # O jogo roda até sobrar apenas 1 pessoa
    while len(fila) > 1:
        # 1. Simula a batata passando de mão em mão
        for _ in range(num_passes):
            # O primeiro da fila "passa a batata" e vai para o fim da roda
            pessoa = fila.popleft() # Sai do início (Dequeue)
            fila.append(pessoa)     # Entra no final (Enqueue)
            
            print(f"Passou! Fila girando: {list(fila)}")
            time.sleep(0.3) # Efeito visual dramático para os alunos
        
        # 2. Quem ficou na frente da fila após K passes é eliminado
        eliminado = fila.popleft()
        print(f"\n💥 BOOM! '{eliminado}' queimou a mao e foi eliminado(a)!\n")
        time.sleep(1)
        
    # 3. O último que sobrou na fila é o vencedor
    vencedor = fila[0]
    return vencedor


def main():
    while True:
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print(" TREINAMENTO DE MARATONA - ESTRUTURA DE DADOS: FILA (FIFO) ")
        print("=" * 60)
        print("1. Jogar Batata Quente")
        print("2. Sair")

        opcao = input("\nDigite sua opcao: ")

        if opcao == "1":
            entrada = input("Digite os nomes separados por virgula (Ex: Ana,Beto,Caio,Dani): ")
            nomes = [nome.strip() for nome in entrada.split(",")]
            
            if len(nomes) <= 1:
                print("ERRO: Precisamos de pelo menos 2 pessoas para o jogo!")
                continue

            try:
                passes = int(input("Numero de passes por rodada (K): "))
            except ValueError:
                print("ERRO: Digite um numero inteiro para os passes.")
                continue
            
            vencedor = batata_quente(nomes, passes)
            
            print("=" * 50)
            print(f"🏆 VENCEDOR: '{vencedor}' sobreviveu! (Accepted) 🏆")
            print("=" * 50)
            
            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            print("Encerrando... Boa sorte no treino dos alunos!")
            break
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()