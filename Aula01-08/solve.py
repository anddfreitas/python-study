


class Estado:
	def __init__(self, pai, homens, mulheres, barco):
		self.pai = pai
		self.homens = homens
		self.mulheres = mulheres
		self.barco = barco

def mostra_estado(estado):
	print(estado.n)

def estado_inicial():
	return Estado(None, [1,1,1], [1,1,1], -1)

def expande(estado):
	ret = []
	h = estado.homens.copy()
	m = estado.mulheres.copy()
	return 

def objetivo(estado):
	return False

def vazio(lista):
	return len(lista) == 0

def adiciona(filhos, lista):
	return lista + filhos

def recupera(lista):
	return lista.pop(0)

lista = [estado_inicial()]

while(not vazio(lista)):
	atual = recupera(lista)

	mostra_estado(atual)

	if(objetivo(atual)):
		mostra_estado(atual)
		break

	filhos = expande(atual)
	lista = adiciona(filhos, lista)















