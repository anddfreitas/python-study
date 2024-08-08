'''

2 Baldes
O primeiro só pode ter no máximo 3 litros
O segundo só pode ter no máximo 4 litros

Movimentos:
1- Primeiro balde cheio
2- Segundo balde cheio
3- Primeiro balde vazio
4- Segundo balde vazio
5- Transfere o primeiro para o segundo
6- Transfere o segundo para o primeiro

Final: Algum dos dois baldes tem que ter 2 litros

'''

class Estado:
    def __init__ (self, pai, vetor):
        self.pai = pai
        self.vetor = vetor

def estado_inicial():
    return Estado(None, [0,0])

def objetivo(estado):
    return estado.vetor[0] == 2 or estado.vetor[1] == 2

def mostrar(estado):
    if estado == None:
        return
    mostrar(estado.pai)
    print(estado.vetor)

def verifica_movimento(filhos):
    if (filhos[0] >= 0 and filhos[0] <= 3) and (filhos[1] >= 0 and filhos[1] <= 4):
        return True
    return False

def expande (estado):
    aux = []
    ret = []
    tem_no_balde = estado.vetor.copy()

    for filho in [[0, tem_no_balde[1]], [tem_no_balde[0], 0], [3, tem_no_balde[1]], [tem_no_balde[0], 4]]:
        aux.append(filho)

    # Transfere do 0 para o 1
    if tem_no_balde[0] > 0: # Ou seja, o balde 0 não está vazio:
        if tem_no_balde[1] + tem_no_balde[0] == 4:
            aux.append([0, 4])
        if tem_no_balde[1] + tem_no_balde[0] > 4:
            dif = 4 - tem_no_balde[1]
            aux.append([tem_no_balde[0] - dif, tem_no_balde[1] + dif])
        if tem_no_balde[1] + tem_no_balde[0] < 4:
            aux.append([0, tem_no_balde[1] + tem_no_balde[0]])

    # Transfere do 1 para o 0
    if tem_no_balde[1] > 0: # Ou seja, o balde 1 não está vazio:
        if tem_no_balde[1] + tem_no_balde[0] == 3:
            aux.append([3, 0])
        if tem_no_balde[1] + tem_no_balde[0] > 3:
            dif = 3 - tem_no_balde[0]
            aux.append([tem_no_balde[0] + dif, tem_no_balde[1] - dif])
        if tem_no_balde[1] + tem_no_balde[0] < 3:
            aux.append([tem_no_balde[0] + tem_no_balde[1], 0])

    for i in aux:
         if verifica_movimento(i):
              ret.append(Estado(estado, i))

    return ret

def vazio(lista):
    return len(lista) == 0

def adiciona(lista, filhos):
    return lista + filhos

def recupera (lista):
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


