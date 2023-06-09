#funcao basicas

from constantes import (CIMA, BAIXO, DIREITA, ESQUERDA, PEGAR, 
                        estados_limite_cima, estados_limite_baixo, estados_limite_direita, estados_limite_esquerda,
                        estados_pocos, estado_wumpus, estado_ouro,
                        recompensa_poco, recompensa_pegar_ouro, recompensa_estado_vazio, recompensa_wumpus)

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

def novo_estado_guerreiro(estado_guerreiro, acao):
    if acao == CIMA:
        return (estado_guerreiro+4)
    elif acao == BAIXO:
        return (estado_guerreiro-4)
    elif acao == DIREITA:
        return (estado_guerreiro+1)
    elif acao == ESQUERDA:
        return (estado_guerreiro-1)
    else: # PEGAR -> o guerreiro fica no mesmo lugar
        return estado_guerreiro
                
def recompensas(estado_guerreiro, acao):
    if estado_guerreiro in estados_pocos:
        return recompensa_poco
    
    elif estado_guerreiro == estado_wumpus:
        return recompensa_wumpus
    
    elif estado_guerreiro == estado_ouro and acao == PEGAR:
        return recompensa_pegar_ouro
    
    else:
        return recompensa_estado_vazio

