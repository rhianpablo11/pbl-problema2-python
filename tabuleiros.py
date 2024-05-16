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

import commons

'''FUNÇÕES DE PRINT'''
def printjogada(jogadas, lista_jog, loc1, val1, loc2, val2, rodada,  hist, som1,som2):
    hist = commons.historico( jogadas, lista_jog, loc1, val1, loc2, val2, hist, rodada, som1,som2)
    separador()
    for plays in hist:
        print(plays)
    
def printpontuacao(p1,p2, lista_jog):
    print("=" *55)
    p = "Pontuacao" 
    print(f"{p:^50}")
    print("{}{}{}: {}".format("\033[36m",lista_jog[0],"\033[0;0m", p1))
    print("{}{}{}: {}".format("\033[31m",lista_jog[1],"\033[0;0m", p2))
    separador()

def separador():
    print("=" *55)

def revelacao():
    separador()
    print("{:^50}" .format("Revelação das somas dos tabuleiros"))
    separador()

def printmatriz(tab_oc):
    for a in range(len(tab_oc)):
        for b in range(len(tab_oc[a])):
            print(f"[ {tab_oc[a][b]:^3} ]", end=" ")  
        print()

def printmatriz_csoma(tab_oc, tab_re): #A DEPENDER DA SITUAÇÃO PRINTA A MATRIZ OCULTA JUNTO AS SOMAS QUE ERAM PARA ACERTAR
    lista_somas = []
    for c in range(len(tab_oc)):
        for l in range(len(tab_oc[c])):
            print(f"[ {tab_oc[c][l]:^3} ]", end=" ")
        print("--|> {}{:^5}{}".format("\033[36m",sum(tab_re[c]),"\033[0;0m"))
        
        loc = "L{}".format(int(c)+1)
        col = commons.elementosnacoluna(loc, tab_re, len(tab_re))
        lista_somas.append(sum(col))
    
    
    for a in lista_somas:
        print("|_>", end="")
        print("{}{:^4}{}".format("\033[31m", a,"\033[0;0m" ), end=" ")