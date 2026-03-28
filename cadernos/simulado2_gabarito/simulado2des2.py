import sys

def resolver_problema():
    try:
        entrada = input().strip()
    except EOFError:
        return
    
    pilha = []

    for c in entrada:
        if c == '{' or c == '[' or c == '(':
            pilha.append(c)
        else:
            if not pilha:
                return False
            if c == ')' and pilha.pop() != '(':
                return False
            if c == ']' and pilha.pop() != '[':
                return False
            if c == '}' and pilha.pop() != '{':
                return False
            else:
                continue
    if pilha:
        return False
    return True


if __name__ == "__main__":
    if resolver_problema():
        print("S")
    else:
        print("N")