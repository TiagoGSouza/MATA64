# teste codigo de acoes

from constantes import (estados_iniciais, estados_finais, recompensa_acao_nao_permitida, ACOES)
from funcoes import (acao_permitida, PEGAR, estado_ouro, novo_estado_guerreiro, recompensas)
import random
import numpy as np

qt_episodios = 200

melhor_recompensa = 0
vitorias = 0

q_table = np.zeros((16, 5))

# Hiperparametros
alpha = 0.8 #taxa de aprendizado
gamma = 0.8 #fator de desconto
epsilon = 0.9 #parametro que auxilia a decidir entre exploration e explotation 
              #e evitar overfitting (escolha da mesma rota sempre)
epsilon_min = 0.01

tolerancia = 0.00001

#           inicio do treinamento
acoes_exploration = 0
acoes_exploitation = 0
episodios_executados = 0

for episodio in range(qt_episodios):
    recompensa_episodio = 0
    estado_guerreiro = random.choice(estados_iniciais)
    estados_finais_episodios = []
    estados_finais_episodios = estados_finais.copy()
    convergiu = False

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

            if(acao == PEGAR and estado_guerreiro == estado_ouro):
                estados_finais_episodios.append(estado_ouro)

            proximo_estado_guerreiro = novo_estado_guerreiro(estado_guerreiro, acao)

            recompensa_acao = recompensas(proximo_estado_guerreiro, acao)
            recompensa_episodio += recompensa_acao

            q_value_antigo = q_table[estado_guerreiro, acao]
            maior_q_value_prox_estado = np.max(q_table[proximo_estado_guerreiro])

            #média móvel exponencial para atualização dos q-values na q_table
            sample = alpha * (recompensa_acao + gamma * maior_q_value_prox_estado)
            novo_q_value = (1 - alpha) * q_value_antigo + sample
            q_table[estado_guerreiro, acao] = novo_q_value
            
            estado_guerreiro = proximo_estado_guerreiro

            dif = abs(novo_q_value - q_value_antigo)

            if dif < tolerancia:
                convergiu = True
                break

        #se a acao nao for permitida, colocamos uma penalidade muito alta
        #assim, ao executar baseado na q_table, evita o guerreiro de ficar em loop
        else:
            recompensa_acao = recompensa_acao_nao_permitida
            q_value_antigo = q_table[estado_guerreiro, acao]
            maior_q_value_prox_estado = np.max(q_table[estado_guerreiro])

            #média móvel exponencial para atualização dos q-values na q_table
            sample = alpha * (recompensa_acao + gamma * maior_q_value_prox_estado)
            novo_q_value = (1 - alpha) * q_value_antigo + sample
            q_table[estado_guerreiro, acao] = novo_q_value

    episodios_executados += 1
    
    if estado_ouro in estados_finais_episodios:
        vitorias += 1

    if epsilon > epsilon_min:
        epsilon = epsilon - epsilon_min
    
    if convergiu:
        break

#           fim do treinamento
print("--------------Treinamento--------------------------------")
print(f"{episodios_executados} episodios executados de {qt_episodios}")
print("Vitorias: ", vitorias)
print("% vitorias: ", vitorias*100/qt_episodios)
print("Taxa de aprendizado (alpha): ", alpha)
print("Fator de desconto (gamma): ", gamma)
print("Epsilon final: " , epsilon)
print("Acoes exploration: ", acoes_exploration)
print("Acoes exploitation: ", acoes_exploitation)
print("--------------Fim do Treinamento--------------------------")

#               avaliar os valores de q_table
acoes_tomadas_todos_episodios = 0
recompensa_total_episodios = 0
vitorias = 0

for episodio in range(qt_episodios):

    estado_guerreiro = random.choice(estados_iniciais)
    recompensa_episodio = 0
    estados_finais_episodios.clear()
    estados_finais_episodios = estados_finais.copy()

    while estado_guerreiro not in estados_finais_episodios:
        acao = np.argmax(q_table[estado_guerreiro])

        if acao_permitida(estado_guerreiro, acao):
            acoes_tomadas_todos_episodios += 1

            if(acao == PEGAR and estado_guerreiro == estado_ouro):
                estados_finais_episodios.append(estado_ouro)

            proximo_estado_guerreiro = novo_estado_guerreiro(estado_guerreiro, acao)

            recompensa_acao = recompensas(proximo_estado_guerreiro, acao)
            recompensa_episodio += recompensa_acao

            q_value_antigo = q_table[estado_guerreiro, acao]
            maior_q_value_prox_estado = np.max(q_table[proximo_estado_guerreiro])

            #média móvel exponencial para atualização dos q-values na q_table
            novo_q_value = (1 - alpha) * q_value_antigo + alpha * (recompensa_acao + gamma * maior_q_value_prox_estado)
            q_table[estado_guerreiro, acao] = novo_q_value
            
            estado_guerreiro = proximo_estado_guerreiro

    recompensa_total_episodios += recompensa_episodio

    if estado_ouro in estados_finais_episodios:
        vitorias = vitorias + 1

print("--------------Avaliando valores tabela q--------------------------------")

print(f"Resultados apos {qt_episodios} episodes:")
print(f"Quantidade media de acoes tomadas por episodio: {acoes_tomadas_todos_episodios / qt_episodios}")
print(f"Recompensa media por episodio: {recompensa_total_episodios / qt_episodios}")
print("Vitorias: ", vitorias)
print("% vitorias: ", (vitorias/qt_episodios)*100)