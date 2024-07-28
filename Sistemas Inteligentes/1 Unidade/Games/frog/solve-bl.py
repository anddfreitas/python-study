'''

1110222

1 - Se move apenas para a direita
2 - Se move apenas para a esquerda

Objetivo final: 2220111

'''

class Estado():
    def __init__(self, pai, vetor):
        self.pai = pai
        self.vetor = vetor

def estado_inicial():
    return Estado(None, [1,1,1,0,2,2,2])

def objetivo(estado):
    if estado.vetor == [2,2,2,0,1,1,1]:
        return True
    return False

def mostrar(estado):
    print(estado.vetor)
    if estado.pai == None:
        return
    mostrar(estado.pai) # Garante que todos os pais sejam mostrados

def verifica_vazio(estado):
    return estado.vetor.index(0)

def move_direita(estado, i):
    ret = Estado(estado, estado.vetor.copy())
    pos_vazia = verifica_vazio(estado)
    ret.vetor[i], ret.vetor[pos_vazia] = ret.vetor[pos_vazia], ret.vetor[i]
    return ret

def move_esquerda(estado, i):
    ret = Estado(estado, estado.vetor.copy())
    pos_vazia = verifica_vazio(estado)
    ret.vetor[i], ret.vetor[pos_vazia] = ret.vetor[pos_vazia], ret.vetor[i]
    return ret

def expande(estado):
    ret = []
    pos_vazia = verifica_vazio(estado)
    for i in range(len(estado.vetor)):
        dist = i - pos_vazia
        if dist >= -2 and dist < 0 and estado.vetor[i] == 1: # Move direita
            ret.append(move_direita(estado, i))
        if dist <= 2 and dist > 0 and estado.vetor[i] == 2: # Move esquerda
            ret.append(move_esquerda(estado, i))
    return ret
        
atual = estado_inicial()
ret = []
j = 0

print("Expandidos: ")
while (not objetivo(atual)):
    filhos = expande(atual)
    ret = filhos + ret
    atual = ret.pop(0)

    for i in range(len(ret)):
        print(ret[i].vetor)
        j = j + 1
    print()

print("Solução: ")
mostrar(atual)
print (j)





