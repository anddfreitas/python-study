
class Estado:
	def __init__(self, pai, casal, barco):
		self.pai = pai
		self.casal = casal
		self.barco = barco

def mostra_estado(estado):
	if estado == None:
		return
	if estado.pai == None:
		return
	mostra_estado(estado.pai)
	print(estado.casal)

def estado_inicial():
	return Estado(None, [0,0,0,0,0,0], 0)

def verifica_movimento(estado):
# Só existe uma movimentação inválida, que é a mulher ir para um lado em que tem algum outro homem sem ser o dela
	for i in range(3):
		if estado.casal[i] == estado.casal[i+3]:
			continue
		for j in range(3, 6):
			if estado.casal[i] == estado.casal[j]:
				return False
	return True

def move_um(estado, i):
	ret = estado.casal.copy()
	if ret[i] == 0:
		ret[i] = 1
	elif ret[i] == 1:
		ret[i] = 0
	return Estado(estado, ret, 1 - estado.barco)

def move_dois(estado, i, j):
	ret = estado.casal.copy()
	if ret[i] == 0:
		ret[i] = 1
	elif ret[i] == 1:
		ret[i] = 0
	if ret[j] == 0:
		ret[j] = 1
	elif ret[j] == 1:
		ret[j] = 0
	return Estado(estado, ret, 1 - estado.barco)

def expande(estado):
	ret = []
	for i in range (len(estado.casal)):
		if (estado.casal[i] == estado.barco):		
			cop = move_um(estado, i)
			ret.append(cop)

	for i in range (len(estado.casal)):
		for j in range(len(estado.casal)):
			if i != j and j > i:
				if estado.casal[i] == estado.barco and estado.casal[j] == estado.barco:
					cop = move_dois(estado, i, j)
					ret.append(cop)
	filtrados = []
	for i in ret:
		if verifica_movimento(i):
			filtrados.append(i)
	return filtrados

def objetivo(estado):
	return estado.casal == [1,1,1,1,1,1]

def vazio(lista):
	return len(lista) == 0

def adiciona(filhos, lista):
	return lista + filhos

def recupera(lista):
	return lista.pop(0)

# Tratamento de repetição
def iguais(estado1, estado2):
	return estado1.casal == estado2.casal and estado1.barco == estado2.barco

def esta_na_lista(filho, visitados):
	for estado in visitados:
		if(iguais(filho, estado)):
			return True
	return False

lista = [estado_inicial()]
visitados = []

while(not vazio(lista)):
	atual = recupera(lista)

	mostra_estado(atual)

	if(objetivo(atual)):
		print("Solução encontrada:")
		mostra_estado(atual)
		break

	filhos = expande(atual)
	visitados.append(atual)

	filtrados = []

	for filho in filhos:
		if(esta_na_lista(filho, visitados)):
			continue
		filtrados.append(filho)

	lista = adiciona(filtrados, lista)


