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
    return Estado(None, [0, 3, 3])

def objetivo(estado):
    if estado.vetor == [1, 0, 0]:
        return True
    return False

def mostrar(estado):
    if estado.pai == None:
        return
    mostrar(estado.pai)
    print(estado.vetor)

# Um missionário
def um_m_dir(estado):
    ret = Estado(estado, estado.vetor.copy())
    ret.vetor[barco] = 1
    ret.vetor[missionario] = ret.vetor[missionario] - 1
    return ret

# Dois missionários para o lado direito
def dois_m_dir(estado):
    ret = Estado(estado, estado.vetor.copy())
    ret.vetor[barco] = 1
    ret.vetor[missionario] = ret.vetor[missionario] - 2
    return ret

# Um canibal para o lado direito
def um_c_dir(estado):
    ret = Estado(estado, estado.vetor.copy())
    ret.vetor[barco] = 1
    ret.vetor[canibal] = ret.vetor[canibal] - 1
    return ret

# Dois canibais para o lado direito
def dois_c_dir(estado):
    ret = Estado(estado, estado.vetor.copy())
    ret.vetor[barco] = 1
    ret.vetor[canibal] = ret.vetor[canibal] - 2
    return ret

def um_m_um_c_dir(estado):
    ret = Estado(estado, estado.vetor.copy())
    ret.vetor[barco] = 1
    ret.vetor[missionario] = ret.vetor[missionario] - 1
    ret.vetor[canibal] = ret.vetor[canibal] - 1
    return ret

# Para a esquerda
# Um missionário
def um_m_esq(estado):
    ret = Estado(estado, estado.vetor.copy())
    ret.vetor[barco] = 0
    ret.vetor[missionario] = ret.vetor[missionario] + 1
    return ret

# Dois missionários para o lado direito
def dois_m_esq(estado):
    ret = Estado(estado, estado.vetor.copy())
    ret.vetor[barco] = 0
    ret.vetor[missionario] = ret.vetor[missionario] + 2
    return ret

# Um canibal para o lado direito
def um_c_esq(estado):
    ret = Estado(estado, estado.vetor.copy())
    ret.vetor[barco] = 0
    ret.vetor[canibal] = ret.vetor[canibal] + 1
    return ret

# Dois canibais para o lado direito
def dois_c_esq(estado):
    ret = Estado(estado, estado.vetor.copy())
    ret.vetor[barco] = 0
    ret.vetor[canibal] = ret.vetor[canibal] + 2
    return ret

def um_m_um_c_esq(estado):
    ret = Estado(estado, estado.vetor.copy())
    ret.vetor[barco] = 0
    ret.vetor[missionario] = ret.vetor[missionario] + 1
    ret.vetor[canibal] = ret.vetor[canibal] + 1
    return ret

def estado_valido(estado):
    esq_m = estado.vetor[missionario]
    esq_c = estado.vetor[canibal]
    dir_m = 3 - esq_m
    dir_c = 3 - esq_c
    
    if (esq_m > 0 and esq_m < esq_c) or (dir_m > 0 and dir_m < dir_c):
        return False
    return True

def expande(estado):
    ret = []
    missionarios = estado.vetor[missionario]
    canibais = estado.vetor[canibal]

    if estado.vetor[0] == 0:

        if missionarios >= 1:
            novo_estado = um_m_dir(estado)
            if estado_valido(novo_estado):
                ret.append(novo_estado)

        if missionarios >= 2:
            novo_estado = dois_m_dir(estado)
            if estado_valido(novo_estado):
                ret.append(novo_estado)

        if canibais >= 1:
            novo_estado = um_c_dir(estado)
            if estado_valido(novo_estado):
                ret.append(novo_estado)

        if canibais >= 2:
            novo_estado = dois_c_dir(estado)
            if estado_valido(novo_estado):
                ret.append(novo_estado)

        if missionarios >= 1 and canibais >= 1:
            novo_estado = um_m_um_c_dir(estado)
            if estado_valido(novo_estado):
                ret.append(novo_estado)

    if estado.vetor[0] == 1:

        if missionarios < 3:
            novo_estado = um_m_esq(estado)
            if estado_valido(novo_estado):
                ret.append(novo_estado)

        if missionarios < 2:
            novo_estado = dois_m_esq(estado)
            if estado_valido(novo_estado):
                ret.append(novo_estado)

        if canibais < 3:
            novo_estado = um_c_esq(estado)
            if estado_valido(novo_estado):
                ret.append(novo_estado)

        if canibais < 2:
            novo_estado = dois_c_esq(estado)
            if estado_valido(novo_estado):
                ret.append(novo_estado)

        if missionarios < 3 and canibais < 3:
            novo_estado = um_m_um_c_esq(estado)
            if estado_valido(novo_estado):
                ret.append(novo_estado)

    return ret

atual = estado_inicial()
ret = []

while (not objetivo(atual)):
    filhos = expande(atual)
    ret = ret + filhos
    atual = ret.pop(0)

mostrar(atual)