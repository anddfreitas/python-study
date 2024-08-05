'''

[0, 3, 3]
[0] = Posição do barco, 0 = esquerda, 1 = direita;
[1] = Quantidade de missionários;
[2] = Quantidade de canibais.

Estado inicial = [0, 3, 3]
Estado final = [1, 0, 0]

Movimentos possíveis = 5

Não pode haver mais canibais que missionários no mesmo lado

'''

barco = 0
missionario = 1
canibal = 2

class Estado():
    def __init__(self, pai, vetor):
        self.pai = pai
        self.vetor = vetor

def estado_inicial():
    return Estado(None, [3,3,-1])

def objetivo(estado):
    if estado.vetor == [0,0,1]:
        return True
    return False

def mostrar(estado):
    if estado.pai == None:
        return
    mostrar(estado.pai)
    print(estado.vetor)

def expande(estado):
    ret = []
    pai = estado.vetor.copy()
    b = pai[2]
    for caso in [[b,b], [2*b,0], [b,0], [0, b], [0, 2*b]]:
        filho = [pai[0] + caso[0], pai[1] + caso[1], b*(-1)]
        if filho[0] >= 0 and filho[0] <= 3 and filho[1] >= 0 and filho[1] <= 3 and filho[0] >= filho[1]:
            ret.append(Estado(estado, filho))
    return ret

atual = estado_inicial()
ret = []

while (not objetivo(atual)):
    filhos = expande(atual)
    ret = ret + filhos
    atual = ret.pop(0)

mostrar(atual)