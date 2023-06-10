from constantes_busca import *
from funcoes_busca import *


def bfs(arvore, vertice_inicial, estado_final): #Implementação mais otimizada da busca em largura ao retornar o primeiro caminho ótimo encontrado e não expandir nós já visitados
    visitados = set()
    fila = [[vertice_inicial]] #Mantem controle em termos de todo o caminho ate o vertice, não só ele
    while fila:
        path = fila.pop(0)
        vertice = path[len(path)-1]
        if vertice not in visitados: #Evita expandir nós já visitados pois se está em já visitado o nó foi visitado em nivel alterior, o que significa que o caminho atual, ao visitar esse nó, não levará ao caminho ótimo, poderemos atingir esse mesmo nó de forma mais otimizada
            vizinhos = arvore[vertice]
            for item in vizinhos:
                novo_path = path.copy()
                novo_path.append(item)
                fila.append(novo_path.copy())

                if item == estado_final:
                    return novo_path #Retorna o primeiro caminho que atinge o estado final. Como a busca é em largura qualquer outro caminho estará em mesmo nível ou abaixo, sendo esse um caminho ótimo

            visitados.add(vertice)
    print("Nao ha caminho ao estado final")

arvore = []
arvore = gera_arvore(arvore)
print(arvore)
result = bfs(arvore, 0, 9)
print(result)

#Melhorar impressao
