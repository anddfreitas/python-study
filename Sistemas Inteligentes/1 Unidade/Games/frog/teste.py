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
    if estado.pai == None:
        return
    mostrar(estado.pai) # Garante que todos os pais sejam mostrados
    print(estado.vetor)

def verifica_vazio(estado):
    return estado.vetor.index(0)

def expande(estado):
    ret = []
    pos_vazia = verifica_vazio(estado)
    for i in range(7):
        armazena = estado.vetor.copy() # Armazena o vetor atual para poder ser alterado sem modificar o original 
        dist = i - pos_vazia # Verifica a distância do sapo com a casa vazia
        if (dist >= -2 and dist < 0 and estado.vetor[i] == 1) or (dist <= 2 and dist > 0 and estado.vetor[i] == 2):
            armazena[i], armazena[pos_vazia] = armazena[pos_vazia], armazena[i]
            ret.append(Estado(estado, armazena))
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





