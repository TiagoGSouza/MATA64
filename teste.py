# teste codigo de acoes

from funcoes import (estados_finais, ACOES, acao_permitida, PEGAR, estado_ouro, novo_estado_guerreiro, recompensas)
import random
import numpy as np

qt_episodios = 10000

melhor_recompensa = 0
melhor_episodio = 0
qt_acoes_melhor_episodio = 0
estado_final_melhor_episodio = 0
vitorias = 0

q_table = np.zeros((16, 5))

# Hyperparameters
alpha = 0.9 #taxa de aprendizado
gamma = 0.75 #fator de desconto
epsilon = 1.0 #parametro que auxilia a decidir entre exploration e explotation 
              #e evitar overfitting (escolha da mesma rota sempre)
epsilon_min = 0.01

acoes_exploration = 0
acoes_exploitation = 0

for episodio in range(qt_episodios):
    recompensa_episodio = 0
    acoes_tomadas_episodio = 0
    estado_final_episodio = 0
    estado_guerreiro = 0
    estados_finais_episodios = estados_finais
    pegou_ouro = False
    todas_acoes = []
    todas_recompensas = []
    todos_estados = [0]

    while estado_guerreiro not in estados_finais_episodios:

        # exploration
        if random.uniform(0, 1) < epsilon:
            acao = random.choice(ACOES)
            acoes_exploration += 1
        #exploitation
        else:
            acao = np.argmax(q_table[estado_guerreiro])
            acoes_exploitation += 1

        if acao_permitida(estado_guerreiro, acao):
            acoes_tomadas_episodio += 1
            todas_acoes.append(acao)

            if(acao == PEGAR and estado_guerreiro == estado_ouro):
                estados_finais_episodios.append(estado_ouro)

            proximo_estado_guerreiro = novo_estado_guerreiro(estado_guerreiro, acao)

            todos_estados.append(proximo_estado_guerreiro)

            recompensa_acao = recompensas(proximo_estado_guerreiro, acao)
            todas_recompensas.append(recompensa_acao)
            recompensa_episodio += recompensa_acao

            q_value_antigo = q_table[estado_guerreiro, acao]
            maior_q_value_prox_estado = np.max(q_table[proximo_estado_guerreiro])

            #média móvel exponencial para atualização dos q-values na q_table
            sample = alpha * (recompensa_acao + gamma * maior_q_value_prox_estado)
            novo_q_value = (1 - alpha) * q_value_antigo + sample
            q_table[estado_guerreiro, acao] = novo_q_value
            
            estado_guerreiro = proximo_estado_guerreiro
            estado_final_episodio = estado_guerreiro

    if epsilon > epsilon_min:
        epsilon = epsilon - 0.01
    
    if recompensa_episodio > 0:
        vitorias = vitorias + 1

    if(recompensa_episodio > melhor_recompensa or melhor_episodio == 0):
        melhor_recompensa = recompensa_episodio
        estado_final_melhor_episodio = estado_final_episodio
        melhor_episodio = episodio
        qt_acoes_melhor_episodio = acoes_tomadas_episodio
        todas_acoes_melhor_episodio = todas_acoes
        todas_recompensas_melhor_episodio = todas_recompensas
        todos_estados_melhor_episodio = todos_estados

print("------------------------------------------------")

print("Episodio escolhido: ", melhor_episodio)
print("Recompensa: ", melhor_recompensa)
print("Acoes: ", qt_acoes_melhor_episodio)
print("Estado final: ", estado_final_melhor_episodio)

print(todos_estados_melhor_episodio)
print(todas_acoes_melhor_episodio)
print(todas_recompensas_melhor_episodio)

print("Estados finais: ", estados_finais)
print("Vitorias: ", vitorias)
print("% vitorias: ", vitorias/qt_episodios)

print("Epsilon final: " , epsilon)
print("Acoes exploration: ", acoes_exploration)
print("Acoes exploitation: ", acoes_exploitation)


print("------------------------------------------------")

acoes_tomadas_todos_episodios = 0
recompensa_total_episodios = 0

for episodio in range(qt_episodios):
    estado_final_episodio = 0
    estado_guerreiro = 0
    recompensa_episodio = 0
    estados_finais_episodios = estados_finais
    pegou_ouro = False

    while estado_guerreiro not in estados_finais_episodios:

        acao = np.argmax(q_table[estado_guerreiro])

        if acao_permitida(estado_guerreiro, acao):
            acoes_tomadas_todos_episodios += 1

            if(acao == PEGAR and estado_guerreiro == estado_ouro):
                estados_finais_episodios.append(estado_ouro)

            proximo_estado_guerreiro = novo_estado_guerreiro(estado_guerreiro, acao)

            recompensa_acao = recompensas(proximo_estado_guerreiro, acao)
            recompensa_episodio += recompensa_acao
            recompensa_total_episodios += recompensa_acao

            q_value_antigo = q_table[estado_guerreiro, acao]
            maior_q_value_prox_estado = np.max(q_table[proximo_estado_guerreiro])

            #média móvel exponencial para atualização dos q-values na q_table
            novo_q_value = (1 - alpha) * q_value_antigo + alpha * (recompensa_acao + gamma * maior_q_value_prox_estado)
            q_table[estado_guerreiro, acao] = novo_q_value
            
            estado_guerreiro = proximo_estado_guerreiro
            estado_final_episodio = estado_guerreiro
    
    if recompensa_episodio > 0:
        vitorias = vitorias + 1

print(f"Results after {qt_episodios} episodes:")
print(f"Average timesteps per episode: {acoes_tomadas_todos_episodios / qt_episodios}")
print(f"Average reward per episode: {recompensa_total_episodios / qt_episodios}")