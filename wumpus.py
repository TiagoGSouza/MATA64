
import random
#inicializar ambiente, acoes, estados, recompensas, transicoes
#   estados
# 12 13 14 15
# 8  9  10 11
# 4  5  6  7
# 0  1  2  3

# se state == 0 || 4 || 8 || 12 -> nao posso mover para esquerda
# se state == 3 || 7 || 11 || 14 -> nao posso mover para direita
# se state == 0 || 1 || 2 || 3 -> nao posso mover para baixo
# se state == 12 || 13 || 14 || 15 -> nao posso mover para cima

estados_limite_cima = [12, 13, 14, 15]
estados_limite_baixo = [0, 1, 2, 3]
estados_limite_direita = [3, 7, 11, 15]
estados_limite_esquerda = [0, 4, 8, 12]

# V V V P
# W O P V
# V V V V
# I V P V

# V -> espaço vazio
# W -> wumpus
# P -> poço
# I -> posicao inicial do guerreiro

global estado_ouro
global estado_wumpus
global estados_pocos

estado_ouro = 9
estado_wumpus = 8
estados_pocos = [2, 10, 15]

#   estado final
#   pode ser o ouro, wumpus vivo ou poços

estados_finais = [2, 8, 10, 15]

#Faces possíveis
# N = 1
# O = 2
# L = 3
# S = 4

# acoes
CIMA = 1
BAIXO = 2
DIREITA = 3
ESQUERDA = 4
ATIRAR = 5
PEGAR = 6
ACOES = [CIMA, BAIXO, DIREITA, ESQUERDA, ATIRAR, PEGAR]

#   recompensas
recompensa_estado_vazio = (-1)
recompensa_poco = (-100)
recompensa_wumpus = (-100)
recompensa_matar_wumpus = 50
recompensa_pegar_ouro = 500
#funcao basicas

def acao_permitida(estado_guerreiro, acao):
    if acao == CIMA and estado_guerreiro in estados_limite_cima:
        return False
    elif acao == BAIXO and estado_guerreiro in estados_limite_baixo:
        return False
    elif acao == DIREITA and estado_guerreiro in estados_limite_direita:
        return False
    elif acao == ESQUERDA and estado_guerreiro in estados_limite_esquerda:
        return False
    else:
        return True

def novo_estado_guerreiro(estado_guerreiro, face_guerreiro, acao):
    if acao == CIMA:
        face_guerreiro = 1
        return (estado_guerreiro+4), face_guerreiro
    elif acao == BAIXO:
        face_guerreiro = 4
        return (estado_guerreiro-4), face_guerreiro
    elif acao == DIREITA:
        face_guerreiro = 3
        return (estado_guerreiro+1), face_guerreiro
    elif acao == ESQUERDA:
        face_guerreiro = 2
        return (estado_guerreiro-1), face_guerreiro
    else: # guerreiro atirou ou 'pegou' o ouro
        return estado_guerreiro, face_guerreiro
  
def flecha_mata_wumpus(estado_guerreiro, face_guerreiro, wumpus_vivo, flechas_guerreiro):
    if not wumpus_vivo:
        return False
    
    if flechas_guerreiro == 0:
        return False
    
    estado_flecha = estado_guerreiro

    if face_guerreiro == 1: #guerreiro esta olhando pro norte
        while estado_flecha not in estados_limite_cima:
            if(estado_flecha == estado_wumpus):
                wumpus_vivo = False
                return True
            estado_flecha += 4
        return False
    
    elif face_guerreiro == 2: #guerreiro esta olhando pra esquerda
        while estado_flecha not in estados_limite_esquerda:
            if(estado_flecha == estado_wumpus):
                wumpus_vivo = False
                return True
            estado_flecha -= 1
        return False
    
    elif face_guerreiro == 3: #guerreiro esta olhando pra direita
        while estado_flecha not in estados_limite_direita:
            if(estado_flecha == estado_wumpus):
                wumpus_vivo = False
                return True
            estado_flecha += 1
        return False
    
    else: #guerreiro esta olhando pro sul
        while estado_flecha not in estados_limite_baixo:
            if(estado_flecha == estado_wumpus):
                wumpus_vivo = False
                return True
            estado_flecha -= 4
        return False
                
def recompensas(estado_guerreiro, acao, flechas_guerreiro, wumpus_vivo):
    if estado_guerreiro in estados_pocos:
        return recompensa_poco, 0
    
    elif estado_guerreiro == estado_wumpus and wumpus_vivo:
        return recompensa_wumpus, 0
    
    elif estado_guerreiro == estado_ouro and acao == PEGAR:
        return recompensa_pegar_ouro, 0
    
    elif acao == ATIRAR:
        if flecha_mata_wumpus(estado_guerreiro, face_guerreiro, wumpus_vivo, flechas_guerreiro):
            return recompensa_matar_wumpus, 1
        else:
            return recompensa_estado_vazio, 0
    
    else:
        return recompensa_estado_vazio, 0
# teste codigo de acoes

qt_episodios = 50

melhor_recompensa = 0
melhor_episodio = 0
qt_acoes_melhor_episodio = 0
estado_final_melhor_episodio = 0

for episodio in range(qt_episodios):
# if(True):
    recompensa_episodio = 0
    acoes_tomadas_episodio = 0
    estado_final_episodio = 0
    estado_guerreiro = 0
    flechas_guerreiro = 1
    face_guerreiro = 3
    pegou_ouro = False
    wumpus_vivo = True
    todas_acoes = []
    todas_recompensas = []
    todos_estados = [0]

    if estado_wumpus not in estados_finais:
        estados_finais.append(estado_wumpus)

    #print(f"------EPISODIO {episodio}------")

    while estado_guerreiro not in estados_finais:

        # exploration
        acao = random.choice(ACOES)
        if acao_permitida(estado_guerreiro, acao):
            acoes_tomadas_episodio += 1
            todas_acoes.append(acao)
            estado_guerreiro, face_guerreiro = novo_estado_guerreiro(estado_guerreiro, face_guerreiro, acao)

            if(acao == PEGAR and estado_guerreiro == estado_ouro):
                pegou_ouro == True

        # print("Acao: ", acao)
        # print("Estado inicial: ", estado_guerreiro)
        # print("Face guerreiro inicial: ", face_guerreiro)

            todos_estados.append(estado_guerreiro)

            recompensa_acao, matou_wumpus = recompensas(estado_guerreiro, acao, flechas_guerreiro, wumpus_vivo)
            todas_recompensas.append(recompensa_acao)

            if matou_wumpus:
                wumpus_vivo = False
        
            if not wumpus_vivo:
                if estado_wumpus in estados_finais:
                    estados_finais.remove(estado_wumpus)
            
            #print("Valor wumpus vivo:", wumpus_vivo)
            #print("Estado atingido:", estado_guerreiro)
            #print("Recompensa no vetor:", todas_recompensas[len(todas_recompensas)-1])
            #print("Soma:", recompensa_episodio, " + ", recompensa_acao)
            recompensa_episodio += recompensa_acao
            #print(recompensa_episodio)

            if acao == ATIRAR:
                flechas_guerreiro = 0

            if estado_guerreiro == estado_ouro and acao == PEGAR:
                estados_finais.append(estado_ouro)
            # print("Novo estado: ", estado_guerreiro)
            # print("Nova face guerreiro: ", face_guerreiro)
            # print(recompensa)
            estado_final_episodio = estado_guerreiro
    # print(recompensa_episodio)
    # print(acoes_tomadas_episodio)
    # print(estado_final_episodio)

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
print(todas_acoes_melhor_episodio)
print(todos_estados_melhor_episodio)
print(todas_recompensas_melhor_episodio)