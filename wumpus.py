# teste codigo de acoes
from constantes import *
from funcoes import *
import random

qt_episodios = 50

melhor_recompensa = 0
melhor_episodio = 0
qt_acoes_melhor_episodio = 0
estado_final_melhor_episodio = 0

for episodio in range(qt_episodios):
    recompensa_episodio = 0
    acoes_tomadas_episodio = 0
    estado_final_episodio = 0
    estado_guerreiro = 0
    estados_finais_episodios = estados_finais
    face_guerreiro = 3
    pegou_ouro = False
    todas_acoes = []
    todas_recompensas = []
    todos_estados = [0]

    while estado_guerreiro not in estados_finais:

        # exploration
        acao = random.choice(ACOES)
        if acao_permitida(estado_guerreiro, acao):
            acoes_tomadas_episodio += 1
            todas_acoes.append(acao)

            if(acao == PEGAR and estado_guerreiro == estado_ouro):
                estados_finais.append(estado_ouro)

            estado_guerreiro_novo, face_guerreiro = novo_estado_guerreiro(estado_guerreiro, face_guerreiro, acao)

            todos_estados.append(estado_guerreiro_novo)

            recompensa_acao = recompensas(estado_guerreiro_novo, acao)
            todas_recompensas.append(recompensa_acao)
            
            recompensa_episodio += recompensa_acao
            
            estado_guerreiro = estado_guerreiro_novo
            estado_final_episodio = estado_guerreiro

    if(recompensa_episodio > melhor_recompensa or melhor_episodio == 0):
        melhor_recompensa = recompensa_episodio
        estado_final_melhor_episodio = estado_final_episodio
        melhor_episodio = episodio
        qt_acoes_melhor_episodio = acoes_tomadas_episodio
        todas_acoes_melhor_episodio = todas_acoes
        todas_recompensas_melhor_episodio = todas_recompensas
        todos_estados_melhor_episodio = todos_estados

print("Episodio escolhido: ", melhor_episodio)
print("Recompensa: ", melhor_recompensa)
print("Acoes: ", qt_acoes_melhor_episodio)
print("Estado final: ", estado_final_melhor_episodio)

print(todos_estados_melhor_episodio)
print(todas_acoes_melhor_episodio)
print(todas_recompensas_melhor_episodio)

print("Estados finais: ", estados_finais)
