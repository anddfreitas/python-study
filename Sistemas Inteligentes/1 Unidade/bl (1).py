

labirinto = [
['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G', 'x'],
['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

class Estado:
	def __init__(self, pai, linha, coluna):
		self.linha = linha
		self.coluna = coluna
		self.pai = pai

def mostra_estado(estado):
	print(f'({estado.linha},{estado.coluna})')

def estado_inicial():
	return Estado(None, 1, 1)

def expande(estado):
	ret = []
	linha = estado.linha
	coluna = estado.coluna
	if(labirinto[linha][coluna-1] != 'x'): # Movimenta para esquerda
		ret.append(Estado(estado, linha, coluna - 1))
	if(labirinto[linha][coluna+1] != 'x'): # Movimenta para direita
		ret.append(Estado(estado, linha, coluna + 1))
	if(labirinto[linha-1][coluna] != 'x'): # Movimenta para cima
		ret.append(Estado(estado, linha - 1, coluna))
	if(labirinto[linha+1][coluna] != 'x'): # Movimenta para baixo
		ret.append(Estado(estado, linha + 1, coluna))
	return ret

def objetivo(estado):
	return labirinto[estado.linha][estado.coluna] == 'G'

def mostra_caminho(estado):
	if(estado == None):
		return
	labirinto[estado.linha][estado.coluna] = '#'
	mostra_caminho(estado.pai)
	mostra_estado(estado)

def vazio(lista):
	return len(lista) == 0

def adiciona(filhos, lista):
	return lista + filhos

def recupera(lista):
	return lista.pop(0)

def iguais(estado1, estado2):
	return estado1.linha == estado2.linha and estado1.coluna == estado2.coluna

def esta_em_ancestrais(filho, pai):
	if(pai == None):
		return False
	if(iguais(filho, pai)):
		return True
	return esta_em_ancestrais(filho, pai.pai)

def esta_na_lista(filho, fronteira):
	for estado in fronteira:
		if(iguais(filho, estado)):
			return True
	return False

lista = [estado_inicial()]
visitados = []

# print("Explorando estados: ")
while(not vazio(lista)):
	atual = recupera(lista)

	# mostra_estado(atual)

	if(objetivo(atual)):
		print("Solução encontrada: ")
		mostra_caminho(atual)
		for linha in labirinto:
			print(linha)
		break

	filhos = expande(atual)
	visitados.append(atual)

	filtrados = []
	for filho in filhos:
		# if(esta_em_ancestrais(filho, atual)):
		# 	continue
		# if(esta_na_lista(filho, lista)):
		# 	continue
		if(esta_na_lista(filho, visitados)):
			continue

		filtrados.append(filho)

		# if(not esta_em_ancestrais(filho, atual)):
		# 	filtrados.append(filho)


	lista = adiciona(filtrados, lista)
