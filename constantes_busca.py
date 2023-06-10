estados_limite_cima = [12, 13, 14, 15, 6, 11, 4]
estados_limite_baixo = [0, 1, 2, 3, 6, 14, 12]
estados_limite_direita = [3, 7, 11, 15, 1, 9, 14]
estados_limite_esquerda = [0, 4, 8, 12, 3, 11, 9]
#Poços e wumpus são considerados como barreiras

# 12 13 14 15
# 8  9  10 11
# 4  5  6  7
# 0  1  2  3

#estado_wumpus = 8 OK
#estados_pocos = [2, 10, 15] 2 OK 10 OK 15 OK

estado_final = 9

global estado_guerreiro
estado_guerreiro = 0

CIMA = 0
BAIXO = 1
DIREITA = 2
ESQUERDA = 3
ACOES = [CIMA, BAIXO, DIREITA, ESQUERDA]