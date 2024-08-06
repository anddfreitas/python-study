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
    return Estado(None, [3,3,-1]) # 4 Missionarios; 3 Canibais; Barco a esquerda

def objetivo(estado):
    return estado.vetor == [0,0,1]

def mostrar(estado):
    if estado == None:
        return
    mostrar(estado.pai)
    print(estado.vetor)

def verifica_movimento(filho):
    max_m = 3
    max_c = 3
    dir = [max_m - filho[0], max_c - filho[1]]
    if (filho[0] >= 0 and filho[1] >= 0 and filho[0] <= 3 and filho[1] <= 3):
        # if (filho[0] >= filho[1] or dir[0] >= dir[1]):
        if (filho[0] != 0 and filho[0] < filho[1]):
            return False
        
        elif (filho[0] != 3 and dir[0] < dir[1]):
            return False
        
        return True
    
    return False

def expande(estado):
    ret = []
    pai = estado.vetor.copy()
    b = pai[2]
    for caso in [[b,b], [2*b,0], [b,0], [0, b], [0, 2*b]]:
        filho = [pai[0] + caso[0], pai[1] + caso[1], b*(-1)]
        if verifica_movimento(filho):
            ret.append(Estado(estado, filho))

    return ret


    # verifica = []

    # for ver in ret:
    #     if verifica_movimento(ver):
    #         verifica.append(ver)

    # return verifica

def vazio(lista):
    return len(lista) == 0

def adiciona(filhos, lista):
    return lista + filhos

def recupera(lista):
    return lista.pop(0)

#Tratamento de repetição
def iguais(estado1, estado2):
	return estado1.vetor == estado2.vetor

def esta_na_lista(filho, visitados):
	for estado in visitados:
		if(iguais(filho, estado)):
			return True
	return False

lista = [estado_inicial()]
visitados = []

while(not vazio(lista)):
	atual = recupera(lista)

	# mostrar(atual)

	if(objetivo(atual)):
		print("Solução encontrada:")
		mostrar(atual)
		break

	filhos = expande(atual)
      
	for i in filhos:
		print(i.vetor)

	visitados.append(atual)

	filtrados = []

	for filho in filhos:
		if(esta_na_lista(filho, visitados)):
			continue
		filtrados.append(filho)

	lista = adiciona(filtrados, lista)