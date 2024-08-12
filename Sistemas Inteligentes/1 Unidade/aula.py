class Estado:
	def __init__(self, pai, profundidade, n): # Adicionado o parâmetro profundidade
		self.n = n
		self.pai = pai
		self.profundidade = profundidade

def mostra_estado(estado):
	print(estado.n)

def estado_inicial():
	return Estado(None, 0, 1)

def expande(estado):
	if(estado.n >= 4):
		return []
	profundidade = estado.profundidade + 1
	return [Estado(estado, profundidade, 2*estado.n), Estado(estado, profundidade, 2*estado.n + 1)] # Adicionado a profundidade

def objetivo(estado):
#	return estado.n == 7
    return False

def mostra_caminho(estado):
	if(estado == None):
		return
	mostra_caminho(estado.pai)
	mostra_estado(estado)

def vazio(lista):
	return len(lista) == 0

def adiciona(filhos, lista):
	return filhos + lista # Primeira modificação, era: lista + filhos

def recupera(lista):
	return lista.pop(0)

limite = 2
resolvido = False
profundidade_maxima = 0
maxima_anterior = -1

while(True): # Adicionado

    lista = [estado_inicial()]

    print("Explorando estados: ")
    while(not vazio(lista)):
        atual = recupera(lista)

        mostra_estado(atual)

        if(objetivo(atual)):
            print("Solução encontrada: ")
            mostra_caminho(atual)
            resolvido = True
            break
		
        if(atual.profundidade > profundidade_maxima):
            profundidade_maxima = atual.profundidade


        if(atual.profundidade == limite): # Adicionado, definido limite de profundidade
            continue

        filhos = expande(atual)
        lista = adiciona(filhos, lista)

    if(resolvido):
        break
	
    if(profundidade_maxima == maxima_anterior):
        break

    limite += 1
    maxima_anterior = profundidade_maxima