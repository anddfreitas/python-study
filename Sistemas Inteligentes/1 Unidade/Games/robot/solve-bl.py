'''
000 - Representação

Primeiro bit: 
0 - Esquerda
1 - Direita

Segundo e terceiro bit
0 - Limpo
1 - Sujo

011 - Estado inicial
x00 - Estado final
'''

class Estado():
    def __init__(self, pai, vetor):
        self.pai = pai
        self.vetor = vetor

def estado_inicial():
    return Estado(None, [0,1,1])

def objetivo(estado):
    if estado.vetor[1] == 0 and estado.vetor[2] == 0:
        return True
    return False

def mostrar(estado):
    if estado.pai == None:
        return
    mostrar(estado.pai) # Garante que todos os pais sejam mostrados
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
    if estado.vetor[0] == 0:
        ref.vetor[1] = 0
    elif estado.vetor[0] == 1:
        ref.vetor[2] = 0
    return ref

def expande(estado):
    return [move_direita(estado), move_esquerda(estado), limpar(estado)]

atual = estado_inicial()
ref = []

print("Expandidos: ")
while(not objetivo(atual)):
    filhos = expande(atual)
    ref = ref + filhos  # Fila, o primeiro que entra é o primeiro que sai
    atual = ref.pop(0)

    for i in range(len(ref)): # Mostra todos os estados expandidos
        print(ref[i].vetor)
    print()

print("Solução: ")
mostrar(atual)


