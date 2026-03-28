## 🚀 Desafio: O Editor de Texto do Maromo

### Descrição do Problema
Os alunos da Fatec estão desenvolvendo um editor de texto minimalista para terminais Linux. Uma das funções desse editor é o processamento do caractere #, que funciona como um backspace (apaga o caractere imediatamente anterior).

Sua tarefa é escrever um programa que receba uma string digitada pelo usuário (contendo letras e o caractere #) e exiba como o texto final ficou após todos os apagamentos.

Regra Importante: Se o cursor estiver no início do texto e o usuário digitar #, nada acontece (o backspace é ignorado).
### Exemplos de Entrada e Saída

| Entrada (**String**) | Saída Esperada | Explicação do Caso |
| :--- | :--- | :--- |
| `abc#d` | `abd` | Caso simples: 'c' é removido, 'd' é inserido. |
| `fatec##etec` | `faetec` | Dois backspaces seguidos removem 't' e 'e'. |
| `###python` | `python` | Backspaces no início de uma pilha vazia são ignorados. |
| `abc###` | *(vazio)* | O número de backspaces é igual ou maior que o de letras. |
| `p#y#t#h#o#n#` | *(vazio)* | Cada letra é imediatamente apagada pelo `#` seguinte. |
| `Maratona##o` | `Maratoo` | Removendo 'n' e 'a' para inserir 'o'. |

---

### Solução Técnica em Python

Para maratonas, a performance é chave. Usar `list.pop()` e `list.append()` garante operações em tempo constante $O(1)$.


---

<div style="page-break-after: always;"></div>

# 🚀 Desafio: O Compilador de Mogi

Você foi contratado para ajudar a equipe de desenvolvimento de um novo compilador focado em dispositivos de baixo processamento. Uma das tarefas mais críticas é garantir que as fórmulas matemáticas inseridas pelos usuários não possuam erros de sintaxe no que diz respeito ao fechamento de parênteses `()`, colchetes `[]` e chaves `{}`.

Uma expressão é considerada **bem formada** se:
1.  Todo símbolo de abertura tem um símbolo de fechamento correspondente do mesmo tipo.
2.  Os símbolos são fechados na ordem inversa em que foram abertos (**LIFO - Last In, First Out**).
3.  Não existe símbolo de fechamento sem um de abertura correspondente.

### 📥 Entrada
A entrada consiste em uma única linha contendo uma string (expressão matemática).
* Exemplo: `{[a+b]*c}`

### 📤 Saída
Imprima o caractere **"S"** (maiúsculo) se a expressão estiver sintaticamente correta e **"N"** (maiúsculo) caso contrário.

---

### 📊 Exemplos de Teste

| Entrada (Expressão) | Saída | Explicação |
| :--- | :---: | :--- |
| `(a+b)*[c-d]` | **S** | Todos os pares abrem e fecham corretamente. |
| `{[a+b]*c}` | **S** | Aninhamento correto: `{ [ ] }`. |
| `((a+b)` | **N** | Erro: Sobrou um parêntese aberto (pilha não esvaziou). |
| `[a+b)` | **N** | Erro: Tentou fechar `[` com `)`. |
| `([a+b)]` | **N** | Erro: Ordem incorreta de fechamento. |
| `)a+b(` | **N** | Erro: Começou com fechamento ou fechou sem abrir. |
| `((())` | **N** | Erro: Quantidade de aberturas maior que fechamentos. |

---

### 💡 Lógica com Pilha (Stack)
Para resolver este problema, utilizamos uma **Pilha**:
* Ao encontrar `(`, `[` ou `{`, fazemos um **Push** (empilhamos).
* Ao encontrar `)`, `]` ou `}`, verificamos se a pilha não está vazia e se o topo da pilha é o par de abertura correspondente. Se sim, fazemos um **Pop** (desempilhamos).
* Se ao final do processamento a pilha estiver **vazia**, a expressão é válida.

---




