import math
import random

'''
Têmpera simulada
'''

centros = [(-0.0522422357543455, -2.175934043611756), (-9.115993832489925, 9.87023045780461), (-9.482300285090297, 7.078264062229202), (3.1932672836805516, 2.9371082326924114), (2.084449206025198, 4.360955241076596), (8.629139010285193, -5.029177082554773), (3.008865339249496, -5.8560079102363405), (5.265684215948847, -9.57758282402111), (-2.0204975917620427, -2.7703899513300456), (5.290229660165435, 1.0724472556470062)]




def f(x): # Objetivo
    # dist = 0
    # for i in centros:
    #     dist = dist + math.dist(x, i)
    # return dist
    return 1.0/sum([math.dist(centro, x) for centro in centros])

class Estado:
    def __init__(self, x):
        self.x = x
        self.f = f(x)

def mostra_estado(estado):
    print(f'Posição da usida: {estado.x}, f: {1.0/estado.f}')

def estado_inicial():
    return Estado([random.uniform(-10, 10), random.uniform(-10, 10)])

def melhor(estados):
    return max(estados, key=lambda e: e.f)

def combina(e, melhor_estado):
    alpha = 0.9999
    nova_pos = [0,0]
    nova_pos[0] = alpha * e.x[0] + (1 - alpha) * melhor_estado.x[0]
    nova_pos[1] = alpha * e.x[1] + (1 - alpha) * melhor_estado.x[1]
    return Estado(nova_pos)

def atualiza_estados(estados, melhor_estado):
    return [combina(e, melhor_estado) for e in estados]


estados = [estado_inicial() for _ in range(100)]

while True:
    melhor_estado = melhor(estados)
    mostra_estado(melhor_estado)
    estados = atualiza_estados(estados, melhor_estado)