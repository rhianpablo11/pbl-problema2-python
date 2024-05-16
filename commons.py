'''
/*******************************************************************************
Autor: Rhian Pablo Araujo Almeida
Componente Curricular: Algoritmos I
Concluido em: 22/05/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/
'''

from random import *
from turtle import pos
'''====================================================================='''
'''===============FUNÇÕES DE FUNCIONAMENTO DOS TABULEIRO================'''
'''====================================================================='''

'''CRIAÇÃO DO TABULEIRO OCULTO E REAL'''
def criatab(n):
    geratriz = []
    tab_oc=[]
    tab_re=[]
    tab_elements=[]
    if n==3: 
        geratriz = sample(range(1,31), 9)
        tab_oc = [["x","x","x"],["x","x","x"],["x","x","x"]]
    elif n==4:
        geratriz= sample(range(1,61),16)
        tab_oc = [["x","x","x","x"],["x","x","x","x"],["x","x","x","x"],["x","x","x","x"]]
    else:
        geratriz = sample(range(1,101), 25)
        tab_oc=[["x","x","x","x", "X"],["x","x","x","x", "X"],["x","x","x","x", "X"],["x","x","x","x", "X"],["x","x","x","x", "X"]]
    for a in range(0,n):
        tab_re.append(sample(geratriz, n))
        for i in tab_re[a]:
            geratriz.remove(i)
    
    return tab_oc, tab_re


'''FUNÇÕES DE RECEBIMENTO DE LOCAL E VALOR PARA AS JOGADAS'''
def local(jogador, cor):
    loc = input("Qual posição deseja jogar {}{}{}: " .format(cor, jogador, "\033[0;0m") ).upper()
    return loc

def valor (jogador, cor):
    val_1 = input("{}{}{} valor da soma:".format(cor, jogador,"\033[0;0m"))
    while val_1.isdigit()==False or val_1 == "0":
        print("entrada invalida, por favor digite um numero valido")
        val_1 = input("{}{}{}, qual valor da soma:" .format(cor,  jogador,"\033[0;0m"))
    return int(val_1)



'''VALIDAR A JOGADA'''
def antibug(posicao, tab_oc, tab_re, nivel):
    if len(posicao)>2 or len(posicao)<2:
        return False
    if (posicao[0]!="L" and posicao[0]!="C") or posicao[1].isdigit() == False:
        return False
    if int(posicao[1])>nivel or int(posicao[1])<=0:
        return False
    if posicao[0] == "L":
        if tab_oc[int(posicao[1])-1] == tab_re[int(posicao[1])-1]:
            return False
    elif posicao[0]=="C":
        col_oc = elementosnacoluna(posicao, tab_oc, nivel)
        col_re = elementosnacoluna(posicao, tab_re, nivel)
        if col_oc == col_re:
            return False

def valida(pos1, pos2, val1, val2, tab_oc, tab_re, nivel):
    if pos1==pos2 and val1==val2:
        if pos1[0]=="L":
            sairam=tab_re[int(pos1[1])-1].copy()
            revelados=q_revelarao(sairam, pos1, tab_oc)
            if revelados == 0:
                return False
            else:
                return True
        elif pos1[0]=="C":
            col = elementosnacoluna(pos1, tab_re, nivel)
            sairam = col.copy()
            revelados=q_revelaraocol(sairam, pos1, tab_oc)
            if revelados == 0:
                return False
            else:
                return True
    else:
        return True


'''FUNÇÕES PARA ACHAR OS MAIORES E MENORES ELEMENTOS'''
def elementosnacoluna(local, tab_re, n): #ENCONTRA OS ELEMENTOS NA COLUNA E LISTA ELES
    col = []
    for a in range(0,n):
        col.append(tab_re[a][int(local[1])-1])
    return col

def maiornacoluna(tab_re, local, nivel, tab_oc): #PARA COLUNA
    maior=0
    col = elementosnacoluna(local, tab_re, nivel)
    sairam=col.copy()
    
    for n in range(len(sairam)):
        for a in range(len(tab_oc)):
            try:
                if tab_oc[a][int(local[1])-1] == sairam[n]:
                    sairam.remove(sairam[n])
            except:
                pass
    maior=max(sairam)
    return maior

def menornacoluna(tab_re, local, nivel, tab_oc): #PARA COLUNA
    menor=1000
    col = elementosnacoluna(local, tab_re, nivel)
    sairam=col.copy()
    
    for n in range(len(sairam)):
        for a in range(len(tab_oc)):
            try:
                if tab_oc[a][int(local[1])-1] == sairam[n]:
                    sairam.remove(sairam[n])
            except:
                pass
    menor=min(sairam)
    return menor

def maiornalinha(tab_re, tab_oc, local): #PARA LINHA
    maior = 0
    sairam=tab_re[int(local[1])-1].copy()
    
    for n in range(len(sairam)):
        for a in range(len(tab_oc)):
            try:
                if tab_oc[int(local[1])-1][a] == sairam[n]:
                    sairam.remove(sairam[n])
            except:
                pass
    maior=max(sairam)
    return maior

def menornalinha(tab_re, tab_oc, local): #PARA LINHA
    menor = 1000
    sairam=tab_re[int(local[1])-1].copy()
    
    for n in range(len(sairam)):
        for a in range(len(tab_oc)):
            try:
                if tab_oc[int(local[1])-1][a] == sairam[n]:
                    sairam.remove(sairam[n])
            except:
                pass
    menor=min(sairam)
    return menor

'''RESPONSAVEL POR CALCULAR A SOMA SEJA DA LINHA, OU COLUNA ESCOLHIDA PELO JOGADOR'''
def somas(tab_re, local, nivel):
    soma= 0
    if local[0] =="L":
        soma = sum(tab_re[int(local[1])-1])
    elif local[0]=="C":
        col=elementosnacoluna(local, tab_re, nivel)
        soma = sum(col)
    return soma

'''FUNÇÃO USADA PARA PONTUAÇÃO'''
def pontos(aprox1, aprox2, pontos1, pontos2, l1, tab_oc, tab_re, nivel):
    if aprox1==0:
        if l1[0]=="L":
           
            sairam=tab_re[int(l1[1])-1].copy()
            revelados=q_revelarao(sairam, l1, tab_oc)
            pontos1+=revelados
        if l1[0]=="C" :
            col = elementosnacoluna(l1, tab_re, nivel)
            sairam=col.copy()
            revelados=q_revelaraocol(sairam, l1, tab_oc)
            pontos1+=revelados
    elif aprox1<aprox2:
        pontos1+=1
    
    elif aprox1>aprox2:
        pontos2+=1
    elif aprox1==aprox2:
        pontos1+=1
        pontos2+=1
               
    return pontos1, pontos2

def pontos_j2(aprox2, l2, pontos2, tab_oc, tab_re, nivel):
    if aprox2 ==0:
        if l2[0]=="L":
            sairam=tab_re[int(l2[1])-1].copy()
            revelados=q_revelarao(sairam, l2, tab_oc)
            pontos2+=revelados
        elif l2[0]=="C":
            col = elementosnacoluna(l2, tab_re, nivel)
            sairam=col.copy()
            revelados=q_revelaraocol(sairam, l2, tab_oc)
            pontos2+=revelados
    return pontos2

'''FUNCAO DE REVELAÇÃO NA TABELA OCULTA'''
'''TROCA OS ELEMENTOS OCULTOS PELOS REAIS'''
def trocanaoculta(tab_oc, tab_re, permissor1,  l1, v1,  nivel, total1):
    
    if permissor1==2:
        if l1[0]=="L":
            troca_emlinha(l1,v1, total1, tab_oc, tab_re)
        elif l1[0]=="C":
            troca_emcoluna(l1, v1, nivel, total1, tab_oc, tab_re)



'''CONSTRUÇÃO DO HISTORICO'''
def criadicionario(jogada, lista_jog): #CRIA O DICIONARIO PARA APOS IR GUARDANDO UMA TUPLA DE ELEMENTOS
    jogada={}
    jogada[lista_jog[0]]= " "
    jogada[lista_jog[1]]= " "
    return jogada

def historico(jogadas, lista_jog, loc1, val1, loc2, val2, hist, rodada, som_1, som_2): #COMPILA OS DADOS E ADICIONA EM UMA LISTA
    jog1 = comofoiajogada(val1, som_1)
    jog2 = comofoiajogada(val2, som_2)
    jogadas[lista_jog[0]]=loc1, val1, jog1
    jogadas[lista_jog[1]]=loc2, val2, jog2
    h1 = ("Rodada: {}\n\n{}{}{}, escolheu {}, chutou: {}, e foi {}" .format(rodada, "\033[36m",lista_jog[0],"\033[0;0m",jogadas[lista_jog[0]][0],jogadas[lista_jog[0]][1],jogadas[lista_jog[0]][2]))
    h2=("{}{}{}, escolheu {}, chutou: {}, e foi {}". format("\033[31m",lista_jog[1],"\033[0;0m", jogadas[lista_jog[1]][0],jogadas[lista_jog[1]][1],jogadas[lista_jog[1]][2]))
    sep = "=" *55
    hist.append(h1)
    hist.append(h2)
    hist.append(sep)
    return hist

def comofoiajogada(valor, som): #ANALISA O CHUTE DOS JOGADORES
    jog = ""
    if valor > som:
        jog = "maior que a soma"
    if valor<som:
        jog ="menor que a soma"
    if valor==som:
        jog = "igual a soma"
    return jog


'''FUNCOES PARA ANALISE DE QUEM MAIS SE APROXIMOU E ENTAO'''
'''SABER DE QUAL JOGADOR SERA REALIZADA A ACAO DE REVELAR NA MATRIZ OCULTA'''

def maisproximo( v1, v2, total1, total2): #VERIFICA QUEM MAIS SE APROXIMOU DA SOMA
    analise=0
    analise2=0
    c1 = total1-int(v1)
    analise = abs(c1)
    c2 = total2-int(v2)
    analise2 = abs(c2)
    return analise, analise2

def permissores(analise, analise2): #VER QUEM MAIS SE APROXIMOU, E ENTAO DA A DEVIDA PERMISSAO PARA REALIZAR A ACAO
    permissao1 = 1
    permissao2 =1
    
    if analise<analise2:
        permissao1 = 2
    if analise>analise2:
        permissao2 = 2
    if analise==analise2:
        permissao1=permissao2 = 2
    return permissao1, permissao2



'''FUNÇÕES PARA REVELAR ELEMENTOS'''
def troca_emlinha( pos,valor, total, tab_oc, tab_re): #TROCA OS ELEMENTOS SE A JOGADA TIVER OCORRIDO EM UMA LINHA
    if valor>total:
        maior1 = maiornalinha(tab_re, tab_oc, pos)
        tab_oc[int(pos[1])-1][tab_re[int(pos[1])-1].index(maior1)]=maior1
    elif valor<total:
        menor1 = menornalinha(tab_re, tab_oc, pos)
        tab_oc[int(pos[1])-1][tab_re[int(pos[1])-1].index(menor1)]=menor1
    elif valor==total:
        tab_oc[int(pos[1])-1]=tab_re[int(pos[1])-1]

def troca_emcoluna(pos, valor, nivel, total, tab_oc, tab_re): #TROCA OS ELEMENTOS SE A JOGADA TIVER OCORRIDO EM UMA LINHA
    col = elementosnacoluna(pos, tab_re, nivel)
            
    if valor>total:
        maior = maiornacoluna(tab_re, pos, nivel, tab_oc)
        tab_oc[int(col.index(maior))][int(pos[1])-1]=maior
    elif valor<total:
        menor = menornacoluna(tab_re, pos, nivel, tab_oc)
        tab_oc[int(col.index(menor))][int(pos[1])-1]=menor
    else:
        for q in range(0, nivel):
            tab_oc[q][int(pos[1])-1]=tab_re[q][int(pos[1])-1] 



'''USADAS PARA VER QUANTOS ELEMENTOS AINDA VAI REVELAR COM O ACERTO DA SOMA'''
'''A QUANTIDADE DE CASAS A SE REVELAR DIZ RESPEITO AOS PONTOS'''
def q_revelarao(sairam, local, tab_oc):#PARA LINHA
           
    for n in range(len(sairam)):
        for a in range(len(tab_oc)):
            try:
                if tab_oc[int(local[1])-1][a] == sairam[n]:
                    sairam.remove(sairam[n])
            except:
                pass
    quant = len(sairam)
    return quant

def q_revelaraocol(sairam, local, tab_oc):#PARA COLUNA
           
    for n in range(len(sairam)):
        for a in range(len(tab_oc)):
            try:
                if tab_oc[a][int(local[1])-1] == sairam[n]:
                    sairam.remove(sairam[n])
            except:
                pass
    quant = len(sairam)
    return quant




        