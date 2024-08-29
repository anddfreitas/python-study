'''
O governo de um paÃ­s fictÃ­cio decide instalar uma usina nuclear em seu territÃ³rio de forma a fornecer energia elÃ©trica para alguns centros de distribuiÃ§Ã£o. As coordenadas cartesianas dos centros de distribuiÃ§Ã£o sÃ£o dados em unidades arbitrÃ¡rias na lista 'centros' do arquivo 'esqueleto.py'. Uma vez que a usina for instalada, linhas de distribuiÃ§Ã£o serÃ£o construÃ­das ligando a usina a cada centro de distribuiÃ§Ã£o. O custo de se construir uma linha de distribuiÃ§Ã£o Ã© proporcional Ã  distÃ¢ncia entre a usina e o centro de distribuiÃ§Ã£o ligado pela linha. Deseja-se determinar a posiÃ§Ã£o (coordenadas cartesianas) da usina de modo a minimizar o custo total com a construÃ§Ã£o de linhas de distribuiÃ§Ã£o.
'''

import math
import random

centros = [(-0.0522422357543455, -2.175934043611756), (-9.115993832489925, 9.87023045780461), (-9.482300285090297, 7.078264062229202), (3.1932672836805516, 2.9371082326924114), (2.084449206025198, 4.360955241076596), (8.629139010285193, -5.029177082554773), (3.008865339249496, -5.8560079102363405), (5.265684215948847, -9.57758282402111), (-2.0204975917620427, -2.7703899513300456), (5.290229660165435, 1.0724472556470062)]

def f(x): # Objetivo
    # dist = 0
    # for i in centros:
    #     dist = dist + math.dist(x, i)
    # return dist
    return sum([math.dist(centro, x) for centro in centros])

class Estado:
    def __init__(self, x):
        self.x = x
        self.f = f(x)

def mostra_estado(estado):
    print(estado.x)
    print(estado.f)

def estado_inicial():
    return Estado([random.uniform(-10, 10), random.uniform(-10, 10)])

def muda(estado):
    deltaX = random.uniform(-1,1)
    deltaY = random.uniform(-1,1)
    return Estado([estado.x[0] + deltaX, estado.x[1] + deltaY])

def vizinhos(estado):
    return [muda(estado) for _ in range (10)]

def melhor_sucessor(estado):
    vizinhanca = vizinhos(estado)
    return min(vizinhanca, key=lambda e: e.f)

atual = estado_inicial()
while True:
    vizinho = melhor_sucessor(atual)

    if vizinho.f >= atual.f:
        break

    atual = vizinho

mostra_estado(atual)