"""
Created on Sun Nov 18 12:36:44 2018

@author: SESA489824
"""
'Biblioteca para desenhar o grafo'

import networkx as nx

'Função para desenhar o Grafo'
def printGraph(G):
    pos=nx.spring_layout(G)
    labels = {}
    for idx, node in enumerate(G.nodes()):
        labels[node] = node 
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels, font_size=12)

M_W = input('Digite Quantidade Comptadore e fios: ') #obtem o numero de computadores e fios

#if M_W == '0 0':
    #return 
'Cria um grafo usando a Biblioteca descrita no inicio'
g = nx.DiGraph()

M = int(M_W.split(' ')[0]) #Quantidade de Computadores (Machine) 
W = int(M_W.split(' ')[1]) #Quantidade de Fios (Wires)

ListaVertices = []

for x in range(M - 2):
    ID_M = input('Digite ID computador e Peso: ')#ID computador e Valor de destruição. [M,P] M = Machine, P = Peso
    T = ID_M.split(' ')
    X = T[0]
    P = int(T[1])
    'Atribui vpeso para uma aresta - No caso o computador foi transformado num vertice com 2 arestas'
    g.add_edge((X + 'a'),(X + 'b'),  capacity = P)
    ListaVertices.append(X)

#Esse 'for' é para colocar os valores das arestas
#de acordo com o numero de fios (W) dado na primeira entrada
for x in range(W):
    ID_W = input('Digite vertice inicial, vertice final e peso: ') #Aresta e peso. [X,Y,P] X = ArestaInicial, Y = ArestaFinal, P = Peso
    T = ID_W.split(' ')
    X = T[0]#Origem
    Y = T[1]#Destino
    P = int(T[2])
    if X=='1':
        'Atribui vpeso para uma aresta - Vertice Inicial(Computador do chefe) Liga no inicial da aresta "Quebrada"(Representado pela letra "a")'
        g.add_edge(X, (Y+'a') ,capacity = P)#'função da biblioteca'
    elif Y== str(M):   
        'Atribui vpeso para uma aresta - Final do vertica "Quebrado"Representado pela letra "b") liga no Vertice final(Servidor)'
        g.add_edge((X+'b'), Y, capacity =P)#'função da biblioteca'
    else:
        
         g.add_edge((X+'b'), (Y+'a') ,capacity = P)#'função da biblioteca'

'imprime o grafo, usando a biblioteca'
printGraph(g)

Cut = nx.minimum_cut_value(g,'1',str(M))

print('Valor de Saída: '+ str(Cut))


                

