
estados_limite_cima = [12, 13, 14, 15]
estados_limite_baixo = [0, 1, 2, 3]
estados_limite_direita = [3, 7, 11, 15]
estados_limite_esquerda = [0, 4, 8, 12]

estado_ouro = 9
estado_wumpus = 8
estados_pocos = [2, 10, 15]

estados_finais = [2, 8, 10, 15]

wumpus_vivo = True

global estado_guerreiro
estado_guerreiro = 0
global flechas_guerreiro
flechas_guerreiro = 1

CIMA = 0
BAIXO = 1
DIREITA = 2
ESQUERDA = 3
PEGAR = 4
ACOES = [CIMA, BAIXO, DIREITA, ESQUERDA, PEGAR]

recompensa_estado_vazio = (-1)
recompensa_poco = (-1000)
recompensa_wumpus = (-1000)
recompensa_matar_wumpus = 50
recompensa_pegar_ouro = 1000

