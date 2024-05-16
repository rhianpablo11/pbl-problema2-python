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
import tabuleiros
'''PERGUNTA QUANTIDADE DE RODADAS'''
def num_rodadas(): #RECEBE VALOR VALIDO DE RODADAS PARA O JOGO
    rodadas = input("Quantidade de rodadas:")
    while rodadas.isdigit()==False or rodadas == "0" or (int(rodadas) %2==0):
        print("Entrada invalida, por favor digite um numero ímpar")
        rodadas = input("Quantidade de rodadas:")
    return rodadas

'''FUNCAO QUE FALA QUEM GANHOU, OU SE TEVE EMPATE'''
def printdo_ganhador(pontos1, pontos2, lista_jog):
    if pontos1>pontos2:
        print("Parabens para o(a) jogador 1, {}{}{}, você venceu, com {}{}{} ponto(s)!!!".format("\033[36m",lista_jog[0],"\033[0;0m","\033[36m",pontos1,"\033[0;0m"))
    elif pontos1<pontos2:
        print("Parabens para o(a) jogador 2, {}{}{}, você venceu, com {}{}{} ponto(s)!!!".format("\033[31m",lista_jog[1],"\033[0;0m","\033[31m",pontos2,"\033[0;0m"))
    else:
        print("Parabens aos(as) jogadores(as) {}{}{} e {}{}{}, vocês empataram!!!".format("\033[36m",lista_jog[0],"\033[0;0m","\033[31m",lista_jog[1],"\033[0;0m"))

'''FUNÇÕES RESPONSAVEIS POR CHAMAR OUTRAS DENTRO DO LOOP DO JOGO'''
'''FUNCIONAMENTO COM 1 TABULEIRO'''
def tabunico(lista_jog, nivel, termino):
    hist =[]
    jogada ={}
    p_1 = 0
    p_2=0
    tab_oc, tab_re = commons.criatab(nivel)
    rodada = 1
    jogadas = commons.criadicionario(jogada, lista_jog)
    #LOOP COM CHAMADAS DE FUNÇÕES ATE O TABULEIRO ESTAR COMPLETO
    if termino =="2":
        tabuleiros.printmatriz(tab_oc)
        while tab_oc != tab_re:
            print(tab_re)
            posicao1 = commons.local(lista_jog[0], "\033[36m")
            while commons.antibug(posicao1, tab_oc, tab_re, nivel) == False:
                print("Este local está indisponivel para jogar\nPor favor escolha outro")
                posicao1 = commons.local(lista_jog[0], "\033[36m")
            val1=commons.valor(lista_jog[0], "\033[36m")

            posicao2 = commons.local(lista_jog[1], "\033[31m")
            while commons.antibug(posicao2, tab_oc, tab_re, nivel) == False:
                print("Este local está indisponivel para jogar\nPor favor escolha outro")
                posicao2 = commons.local(lista_jog[1], "\033[31m")
            val2=commons.valor(lista_jog[1], "\033[31m")

            soma1 = commons.somas(tab_re, posicao1, nivel)
            soma2 = commons.somas(tab_re, posicao2, nivel)
            anl_1, anl_2=commons.maisproximo(val1, val2, soma1, soma2)
            perm_1, perm_2 = commons.permissores(anl_1, anl_2)
            p_1, p_2 = commons.pontos(anl_1, anl_2, p_1, p_2, posicao1, tab_oc, tab_re, nivel)
            commons.trocanaoculta(tab_oc, tab_re, perm_1,  posicao1,  val1,   nivel, soma1)
            p_2= commons.pontos_j2(anl_2,  posicao2,p_2, tab_oc, tab_re, nivel)
            if commons.valida(posicao1, posicao2, anl_1, anl_2, tab_oc, tab_re, nivel) ==True:
                commons.trocanaoculta(tab_oc, tab_re, perm_2,  posicao2,  val2,   nivel, soma2)
            tabuleiros.printjogada(jogadas, lista_jog, posicao1, val1,  posicao2, val2, rodada, hist, soma1, soma2)
            tabuleiros.printmatriz(tab_oc)
            tabuleiros.printpontuacao(p_1, p_2, lista_jog)
            rodada+=1
    #LOOP COM CHAMADAS DE FUNÇÕES ATE QUANTIDADE
    #DE RODADAS OU O TABULEIRO ESTAR COMPLETO(CASO FIQUE ANTES DA QUANT DE RODADAS)     
    else:
        n_rodadas = num_rodadas()
        tabuleiros.printmatriz(tab_oc)
        for a in range(int(n_rodadas)):
            if tab_oc != tab_re:
                #print(tab_re)
                posicao1 = commons.local(lista_jog[0], "\033[36m")
                while commons.antibug(posicao1, tab_oc, tab_re, nivel) == False:
                    print("Este local está indisponivel para jogar\nPor favor escolha outro")
                    posicao1 = commons.local(lista_jog[0], "\033[36m")
                val1=commons.valor(lista_jog[0], "\033[36m")

                posicao2 = commons.local(lista_jog[1], "\033[31m")
                while commons.antibug(posicao2, tab_oc, tab_re, nivel) == False:
                    print("Este local está indisponivel para jogar\nPor favor escolha outro")
                    posicao2 = commons.local(lista_jog[1], "\033[31m")
                val2=commons.valor(lista_jog[1], "\033[31m")

                soma1 = commons.somas(tab_re, posicao1, nivel)
                soma2 = commons.somas(tab_re, posicao2, nivel)
                anl_1, anl_2=commons.maisproximo(val1, val2, soma1, soma2)
                perm_1, perm_2 = commons.permissores(anl_1, anl_2)
                p_1, p_2 = commons.pontos(anl_1, anl_2, p_1, p_2, posicao1, tab_oc, tab_re, nivel)
                commons.trocanaoculta(tab_oc, tab_re, perm_1,  posicao1,  val1,   nivel, soma1)
                p_2= commons.pontos_j2(anl_2,  posicao2,p_2, tab_oc, tab_re, nivel)
                if commons.valida(posicao1, posicao2, anl_1, anl_2, tab_oc, tab_re, nivel) ==True:
                    commons.trocanaoculta(tab_oc, tab_re, perm_2,  posicao2,  val2,   nivel, soma2)
                tabuleiros.printjogada(jogadas, lista_jog, posicao1, val1,  posicao2, val2, rodada, hist, soma1, soma2)
                tabuleiros.printmatriz(tab_oc)
                tabuleiros.printpontuacao(p_1, p_2, lista_jog)
                rodada+=1
            else:
                print("O tabuleiro foi completo antes da quantidade de rodadas estipulado")
                break
        if tab_oc!=tab_re:
            tabuleiros.revelacao()
            tabuleiros.printmatriz_csoma(tab_oc, tab_re)
            print()
            tabuleiros.separador()
    printdo_ganhador(p_1, p_2, lista_jog)

'''FUNCIONAMENTO COM 2 TABULEIROS'''
def tabduplo(lista_jog, nivel, termino):
    hist = []
    p_1 = 0
    p_2=0
    jogada={}
    tab_oc, tab_re = commons.criatab(nivel)
    tab_oc2, tab_re2 =commons.criatab(nivel)
    rodada = 1
    jogadas = commons.criadicionario(jogada, lista_jog)
    
    #LOOP COM CHAMADAS DE FUNÇÕES ATE UM DOS TABULEIROS ESTAREM COMPLETOS
    if termino =="2":
        print("Tabela: {}{}{}" .format("\033[36m", lista_jog[0],"\033[0;0m"))
        tabuleiros.printmatriz(tab_oc)
        tabuleiros.separador()
        print("Tabela: {}{}{}" .format("\033[31m", lista_jog[1],"\033[0;0m"))
        tabuleiros.printmatriz(tab_oc2)
        while tab_oc != tab_re and tab_oc2 != tab_re2:
            # print(tab_re)
            # print(tab_re2)

            '''INICIO DO JOGO'''
            posicao1 = commons.local(lista_jog[0], "\033[36m")
            while commons.antibug(posicao1, tab_oc, tab_re, nivel) == False:
                print("Este local está indisponivel para jogar\nPor favor escolha outro")
                posicao1 = commons.local(lista_jog[0], "\033[36m")
            val1=commons.valor(lista_jog[0], "\033[36m")

            posicao2 = commons.local(lista_jog[1], "\033[31m")
            while commons.antibug(posicao2, tab_oc2, tab_re2, nivel) == False:
                print("Este local está indisponivel para jogar\nPor favor escolha outro")
                posicao2 = commons.local(lista_jog[1], "\033[31m")
            val2=commons.valor(lista_jog[1], "\033[31m")

            soma1 = commons.somas(tab_re, posicao1, nivel)
            soma2 = commons.somas(tab_re2, posicao2, nivel)
            anl_1, anl_2=commons.maisproximo(val1, val2, soma1, soma2)
            perm_1, perm_2 = commons.permissores(anl_1, anl_2)
            p_1, p_2 = commons.pontos(anl_1, anl_2, p_1, p_2, posicao1, tab_oc, tab_re, nivel)
            p_2= commons.pontos_j2(anl_2,  posicao2,p_2, tab_oc2, tab_re2, nivel)
            commons.trocanaoculta(tab_oc, tab_re, perm_1, posicao1, val1,  nivel,  soma1)
            commons.trocanaoculta(tab_oc2, tab_re2, perm_2, posicao2, val2,  nivel, soma2)
            tabuleiros.printjogada(jogadas, lista_jog, posicao1, val1,  posicao2, val2, rodada, hist, soma1, soma2)
            tabuleiros.printpontuacao(p_1, p_2, lista_jog)
            print("Tabuleiro: {}{}{}" .format("\033[36m", lista_jog[0],"\033[0;0m"))
            tabuleiros.printmatriz(tab_oc)
            tabuleiros.separador()
            print("Tabuleiro: {}{}{}" .format("\033[31m", lista_jog[1],"\033[0;0m"))
            tabuleiros.printmatriz(tab_oc2)
            rodada+=1
    
    #LOOP COM CHAMADAS DE FUNÇÕES ATE QUANTIDADE DE RODADAS OU UM
    #DOS TABULEIRO ESTAR COMPLETO(CASO FIQUE ANTES DA QUANT DE RODADAS)
    else:
        n_rodadas = num_rodadas()
        print("Tabela: {}{}{}" .format("\033[36m", lista_jog[0],"\033[0;0m"))
        tabuleiros.printmatriz(tab_oc)
        tabuleiros.separador()
        print("Tabela: {}{}{}" .format("\033[31m", lista_jog[1],"\033[0;0m"))
        tabuleiros.printmatriz(tab_oc2)
        for novarodada in range(0, int(n_rodadas)):
            '''INICIO DO JOGO'''
            if tab_oc != tab_re and tab_oc2 != tab_re2:
                # print(tab_re)
                # print(tab_re2)

                '''INICIO DO JOGO'''
                posicao1 = commons.local(lista_jog[0], "\033[36m")
                while commons.antibug(posicao1, tab_oc, tab_re, nivel) == False:
                    print("Este local está indisponivel para jogar\nPor favor escolha outro")
                    posicao1 = commons.local(lista_jog[0], "\033[36m")
                val1=commons.valor(lista_jog[0], "\033[36m")

                posicao2 = commons.local(lista_jog[1], "\033[31m")
                while commons.antibug(posicao2, tab_oc2, tab_re2, nivel) == False:
                    print("Este local está indisponivel para jogar\nPor favor escolha outro")
                    posicao2 = commons.local(lista_jog[1], "\033[31m")
                val2=commons.valor(lista_jog[1], "\033[31m")

                soma1 = commons.somas(tab_re, posicao1, nivel)
                soma2 = commons.somas(tab_re2, posicao2, nivel)
                anl_1, anl_2=commons.maisproximo(val1, val2, soma1, soma2)
                perm_1, perm_2 = commons.permissores(anl_1, anl_2)
                p_1, p_2 = commons.pontos(anl_1, anl_2, p_1, p_2, posicao1, tab_oc, tab_re, nivel)
                p_2= commons.pontos_j2(anl_2,  posicao2,p_2, tab_oc2, tab_re2, nivel)
                commons.trocanaoculta(tab_oc, tab_re, perm_1, posicao1, val1,  nivel,  soma1)
                commons.trocanaoculta(tab_oc2, tab_re2, perm_2, posicao2, val2,  nivel, soma2)
                tabuleiros.printjogada(jogadas, lista_jog, posicao1, val1,  posicao2, val2, rodada, hist, soma1, soma2)
                tabuleiros.printpontuacao(p_1, p_2, lista_jog)
                print("Tabuleiro: {}{}{}" .format("\033[36m", lista_jog[0],"\033[0;0m"))
                tabuleiros.printmatriz(tab_oc)
                tabuleiros.separador()
                print("Tabuleiro: {}{}{}" .format("\033[31m", lista_jog[1],"\033[0;0m"))
                tabuleiros.printmatriz(tab_oc2)
                rodada+=1
            else: 
                print("O tabuleiro foi completo antes da quantidade de rodadas estipulado")
                break

        if tab_oc!=tab_re and tab_oc2 !=tab_re2:
            tabuleiros.revelacao()
            print("Tabuleiro: {}{}{}" .format("\033[36m", lista_jog[0],"\033[0;0m"))
            tabuleiros.printmatriz_csoma(tab_oc, tab_re)
            print()
            tabuleiros.separador()
            print("Tabuleiro: {}{}{}" .format("\033[31m", lista_jog[1],"\033[0;0m"))
            tabuleiros.printmatriz_csoma(tab_oc2, tab_re2)
            print()
            tabuleiros.separador()

        elif tab_oc!= tab_re and tab_oc2 == tab_re2:
            tabuleiros.revelacao()
            print("Tabuleiro: {}{}{}" .format("\033[36m", lista_jog[0],"\033[0;0m"))
            tabuleiros.printmatriz_csoma(tab_oc, tab_re)
            print()
            tabuleiros.separador()

        elif tab_oc==tab_re and tab_oc2!=tab_re2:
            tabuleiros.revelacao()
            print("Tabuleiro: {}{}{}" .format("\033[31m", lista_jog[1],"\033[0;0m"))
            tabuleiros.printmatriz_csoma(tab_oc2, tab_re2)
            print()
            tabuleiros.separador()
    printdo_ganhador(p_1, p_2, lista_jog)



