nomes = [
		"São Miguel",
		"Rafael Fernandes",
		"Pau dos Ferros",
		"Martins",
		"São Francisco do Oeste",
		"Portalegre",
		"Umarizal",
		"Riacho da Cruz",
		"Rodolfo Fernandes",
		"Itaú"
		"Caraúbas",
		"Apodi"
	]

vizinhanca = [
    [1,2],
    [0,2],
    [0,1,3,4,5],
    [2,6],
    [2,9],
    [2,7],
    [3,7,10],
    [5,6,9],
    [9],
    [4,7,8,11],
    [6,11],
    [9,10]
]

class Estado:
	def __init__(self, pai, n, passou7):
		self.n = n
		self.pai = pai
		self.passou7 = passou7

def mostra_estado(estado):
	print(estado.n)

def estado_inicial():
	return Estado(None, 0, False)

def objetivo(estado):
	return estado.n == 10 and estado.passou7 == True

def expande(estado):
	vizinhos = []
	for i in range(len(vizinhanca[estado.n])):
		passou = estado.passou7
		if vizinhanca[estado.n][i] == 7:
			passou = True
		vizinhos.append(Estado(estado, vizinhanca[estado.n][i], passou))
	return vizinhos

def mostra_caminho(estado):
	if(estado == None):
		return
	mostra_caminho(estado.pai)
	mostra_estado(estado)

def vazio(lista):
	return len(lista) == 0

def adiciona(filhos, lista):
	return lista + filhos

def recupera(lista):
	return lista.pop(0)

lista = [estado_inicial()]

print("Explorando estados: ")
while(not vazio(lista)):
	atual = recupera(lista)

	mostra_estado(atual)

	if(objetivo(atual)):
		print("Solução encontrada: ")
		mostra_caminho(atual)
		break

	filhos = expande(atual)
	lista = adiciona(filhos, lista)

	
