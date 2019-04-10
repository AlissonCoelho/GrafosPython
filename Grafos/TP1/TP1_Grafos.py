# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 23:21:38 2018

@author: SESA489824
"""
import math
import networkx as nx
import numpy as np

def DistanciaVet(d1,d2): 
    x = math.sqrt(pow((d1[0]-d2[0]),2) +pow((d1[1]-d2[1]),2))
    return x


def printGraph(G, Pos=None):
    if Pos==None:
        pos=nx.spring_layout(G)
    else:
        pos = Pos
    labels = {}
    for idx, node in enumerate(G.nodes()):
        labels[node] = node 
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels, font_size=12)

NumeroCidades = 0

while ((1<= NumeroCidades <= 1000) == 0):
    
    NumeroCidades = int(input('digite o numero de cidades: '))

    if ((1 <= NumeroCidades <= 1000) == 0):
        print('numero de cidades invalido')

Cidades = []
NomeNos = []

for i in range((NumeroCidades)):
    CordX = float(input('Coordenada x da %s° cidade: ' %(i+1) ))
    CordY = float(input('Coordenada y da %s° cidade: ' %(i+1) ))
    c = [CordX,CordY]
    NomeNos.append('c'+str(i+1))
    Cidades.append(c)

# CRIAR UM GRAFO COMPLETO
g = nx.Graph()

DictPos = {}
for i in range(len(Cidades)):
    Coordenada1 = Cidades[i]
    c = np.array(Coordenada1, float)
    DictPos[NomeNos[i]] = c
    
    for j in range(len(Cidades)): 
        if i < j:
            Coordenada2 = Cidades[j]
            g.add_edge(NomeNos[i],NomeNos[j] , weight= DistanciaVet(Coordenada1,Coordenada2))
            
print("Grafo Completo Vertices: ")
print(g.nodes())
print("Grafo Completo Arestas: ")
print(g.edges())

"""
# imprime UM GRAFO COMPLETO
printGraph(g,DictPos)
"""
AtributsEdges = nx.get_edge_attributes(g, 'weight' ) #retorna um dicionario

Tree = nx.minimum_spanning_tree(g)

ValorEdgesTree = nx.get_edge_attributes(Tree, 'weight' )

Distancia = 0.0

for key in ValorEdgesTree:
    Distancia += ValorEdgesTree[key]

# imprime GRAFO 
printGraph(Tree,DictPos)

print()
print()
print("Vertices Arvore: ")
print(Tree.nodes())
print("Arestas Arvore: ")
print(Tree.edges())
print("Soma das Arestas ou Distancia minima Fibra Otica: ")
print('{:.4f}'.format(Distancia))








