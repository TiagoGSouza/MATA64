from constantes_busca import *

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
    
def gera_arvore(arvore):
    for i in range(16): #para cada estado
        acoes = []
        if i not in [2, 10, 15, 8]:
            if acao_permitida(i, CIMA):
                acoes.append(i+4)

            if acao_permitida(i, BAIXO):
                acoes.append(i-4)

            if acao_permitida(i, DIREITA):
                acoes.append(i+1)

            if acao_permitida(i, ESQUERDA):
                acoes.append(i-1)
        arvore.append(acoes.copy())
    return arvore
        #pode ser melhorado para que os pocoes e wumpus sejam considerados barreiras automaticamente