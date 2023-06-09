#funcao basicas

from constantes import *

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
    else: # guerreiro atirou ou 'pegou' o ouro
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

