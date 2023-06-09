# teste codigo de acoes
from constantes import *
from funcoes import *
import random

qt_episodios = 50

melhor_recompensa = 0
melhor_episodio = 0
qt_acoes_melhor_episodio = 0
flechas_guerreiro = 1

todas_acoes = []
todas_recompensas = []
todos_estados = []

for episodio in range(qt_episodios):
# if(True):
    recompensa_episodio = 0
    acoes_tomadas_episodio = 0
    estado_final_episodio = 0
    estado_guerreiro = 0
    pegou_ouro = False
    flechas_guerreiro = 1
    wumpus_vivo = True
    todas_acoes.clear()
    todas_recompensas.clear()
    todos_estados.clear()

    todos_estados = [0]

    while estado_guerreiro not in estados_finais:
        

        # exploration
        acao = random.choice(ACOES)
        acoes_tomadas_episodio += 1
        todas_acoes.append(acao)

        if(acao == PEGAR and estado_guerreiro == estado_ouro):
            pegou_ouro == True

        # print("Acao: ", acao)
        # print("Estado inicial: ", estado_guerreiro)
        # print("Face guerreiro inicial: ", face_guerreiro)

        if acao_permitida(estado_guerreiro, acao):
            estado_guerreiro, face_guerreiro = novo_estado_guerreiro(estado_guerreiro, face_guerreiro, acao)

        todos_estados.append(estado_guerreiro)

        recompensa_acao, wumpus_vivo = recompensas(estado_guerreiro, acao, flechas_guerreiro, wumpus_vivo)
        todas_recompensas.append(recompensa_acao)
        
        if not wumpus_vivo:
            if estado_wumpus in estados_finais:
                estados_finais.remove(estado_wumpus)

        recompensa_episodio += recompensa_acao

        if acao == ATIRAR:
            flechas_guerreiro = 0

        if estado_guerreiro == estado_ouro and acao == PEGAR:
            estados_finais.append(estado_ouro)
        estado_final_episodio = estado_guerreiro


    if(recompensa_episodio > melhor_recompensa or melhor_episodio == 0):
        melhor_recompensa = recompensa_episodio
        melhor_episodio = episodio
        qt_acoes_melhor_episodio = acoes_tomadas_episodio
        todas_acoes_melhor_episodio = todas_acoes
        todas_recompensas_melhor_episodio = todas_recompensas
        todos_estados_melhor_episodio = todos_estados

# print("Episodio: ", melhor_episodio)
print("Recompensa: ", melhor_recompensa)
print("Acoes: ", qt_acoes_melhor_episodio)
print("Estado final: ", estado_final_episodio)
print(todas_acoes)
print(todos_estados)
print(todas_recompensas)
