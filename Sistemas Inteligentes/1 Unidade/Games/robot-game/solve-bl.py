'''
No jogo há 2 salas, o robô só pode se mover para uma delas por vez, e pode ou não limpar elas.

No jogo há três bits 000 

O primeiro é a posição do robô:
0 - Esquerda
1 - Direita

O segundo e terceiro indicam respectivamente a sala e seu estado:
0 - Limpa
1 - Suja

Estado inicial: 011
Estado final:   x00
'''

class Estado():
    def __init__(self, pai, vetor):
        self.pai = pai
        self.vetor = vetor

def estado_inicial():
    return Estado(None, [0, 1, 1])

def objetivo(estado):
    return estado.vetor[1] == 0 and estado.vetor[2] == 0

def mostrar(estado):
    if (estado.pai == None):
        return
    mostrar(estado.pai)
    print(estado.vetor)

def move_direita(estado):
    ref = Estado(estado, estado.vetor.copy())
    ref.vetor[0] = 1
    return ref

def move_esquerda(estado):
    ref = Estado(estado, estado.vetor.copy())
    ref.vetor[0] = 0
    return ref

def limpar(estado):
    ref = Estado(estado, estado.vetor.copy())
    if ref.vetor[0] == 0:
        ref.vetor[1] = 0
    elif ref.vetor[0] == 1:
        ref.vetor[2] = 0
    return ref

def expandir(estado):
    return [move_direita(estado), move_esquerda(estado), limpar(estado)]

atual = estado_inicial()
ref = []

while not objetivo(atual):
    filhos = expandir(atual)
    ref = ref + filhos

    for i in range(len(ref)):
        print(ref[i].vetor)

    print()

    atual = ref.pop(0)

mostrar(atual)

    