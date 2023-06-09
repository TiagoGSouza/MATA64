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
        return recompensa_poco, True
    
    elif estado_guerreiro == estado_wumpus and wumpus_vivo:
        return recompensa_wumpus, True
    
    elif estado_guerreiro == estado_ouro and acao == PEGAR:
        return recompensa_pegar_ouro, True
    
    elif acao == ATIRAR:
        if flecha_mata_wumpus(estado_guerreiro, face_guerreiro, wumpus_vivo, flechas_guerreiro):
            return recompensa_matar_wumpus, False
        else:
            return recompensa_estado_vazio, True
    
    else:
        return recompensa_estado_vazio, True

