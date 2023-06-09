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
                
def recompensas(estado_guerreiro, acao):
    if estado_guerreiro in estados_pocos:
        return recompensa_poco
    
    elif estado_guerreiro == estado_wumpus:
        return recompensa_wumpus
    
    elif estado_guerreiro == estado_ouro and acao == PEGAR:
        return recompensa_pegar_ouro
    
    else:
        return recompensa_estado_vazio

