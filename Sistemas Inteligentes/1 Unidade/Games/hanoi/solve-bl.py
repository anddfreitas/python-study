

class Estado:
    def __init__ (self, pai, vetor):
        self.pai = pai
        self.vetor = vetor

def estado_inicial():
    return Estado(None, [[3,2,1], [], []])

def objetivo(estado):
    return estado.vetor == [[], [], [3,2,1]]

def mostrar(estado):
    if estado == None:
        return
    mostrar(estado.pai)
    print(estado.vetor[0])
    print(estado.vetor[1])
    print(estado.vetor[2])
    print()

def verifica_movimento(estado, ori, dest):
    if len(estado.vetor[ori]) == 0:
        return False
    if len(estado.vetor[dest]) == 0 or estado.vetor[dest][-1] > estado.vetor[ori][-1]:
        return True
    return False  

def expande(estado):
    ret = []
    for ori in range(len(estado.vetor)):
        for dest in range(len(estado.vetor)):
            if ori != dest and verifica_movimento(estado, ori, dest):
                guarda = [estado.vetor[0].copy(), estado.vetor[1].copy(), estado.vetor[2].copy()]
                r = guarda[ori].pop()
                guarda[dest].append(r)
                ret.append(Estado(estado, guarda.copy()))
    return ret                

def vazio(lista):
    return len(lista) == 0

def adiciona(lista, filhos):
    return lista + filhos

def recupera(lista):
    return lista.pop(0)

lista = [estado_inicial()]

while (not vazio(lista)):
    atual = recupera(lista)

    if objetivo(atual):
        mostrar(atual)
        break

    filhos = expande(atual)
    lista = adiciona(lista, filhos)