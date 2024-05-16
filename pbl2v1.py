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


'''IMPORT'''
import jogo
import tabuleiros
def boasvindas():
    tabuleiros.separador()
    print("\n")
    print("{:^51}" .format("SEJAM BEM-VINDOS(AS) A:"))
    print("{:^51}".format("SOMAS ESQUECIDAS, O JOGO"))
    print("{:^5}" .format(""))
    tabuleiros.separador()
'''FUNÇÕES USADAS PARA AS PERGUNTAS E ESCOLHAS DO MENU'''
def jogadores(): #RECEBER E LISTAR NOME DOS JOGADORES
    lista_jog = []
    cores = ["\033[36m","\033[31m"]
    for a in cores:
        nome_jog = input("Nome do jogador {}: {}" .format((int(cores.index(a))+1), a))
        print("\033[0;0m", end="")
        while nome_jog in lista_jog or nome_jog =="":
            print("Por favor insira um nome valido")
            nome_jog = input("Nome do jogador {}: {}" .format((int(cores.index(a))+1), a))
            print("\033[0;0m", end="")
        lista_jog.append(nome_jog)
        
    return lista_jog

def qual_nivel(): #RECEBER QUAL O NIVEL, E TROCAR O VALOR DA VARIAVEL
    nivel = input("Nivel em que deseja jogar\nEscolha dentre as opcoes abaixo:\n1) Facil - Tabuleiro 3x3\n2) Medio - Tabuleiro 4x4\n3) Dificil - Tabuleiro 5x5\nnivel: ")
    while nivel.isdigit()==False or nivel !="1" and nivel!="2" and nivel!="3":
        print("Opcao invalida, por favor digite um algarismo dentre as opcoes")
        nivel = input("Nivel desejado: ")
    if nivel == "1":
        nivel= 3
    elif nivel =="2":
        nivel=4
    else:
        nivel=5
    return nivel

def q_tabuleiro(): #RECEBER QUANTIDADE DE TABULEIROS PARA SE JOGAR
    q_tab = input("Quantidade de tabuleiros disponiveis para jogar\nÉ possivel jogar com ate 2 tabuleiros\nquantidade desejada: ")
    while q_tab.isdigit()==False or q_tab !="1" and q_tab!="2":
        print("Opcao invalida, por favor digite uma quantidade valida")
        q_tab = input("Quantidade de tabuleiros desejados para jogar")
    return q_tab

def como_para(): #RECEBER A OPCAO DE COMO ENCERRAR A PARTIDA
    termino = input("Como encerrar o jogo\n1) Numero de rodadas\n2) Tabuleiro revelado totalmente\nSua escolha: ")
    while termino.isdigit()==False or termino !="1" and termino!="2":
        print("Opcao invalida, por favor digite um algarismo dentre as opcoes")
        termino = input("Como encerrar o jogo: ")
    return termino

def continua_nao(): #RECEBER "ORDEM" PARA ENCERRAR OU CONTINUAR O JOGO
    opcao = input("O que deseja fazer\n1) Jogar novamente\n2) Encerrar o jogo\nSua escolha: ")
    while opcao !="1" and opcao!="2":
        print("Opcao invalida, por favor digite um algarismo dentre as opcoes")
        opcao = input("O que deseja fazer: ")
    return opcao



'''FUNCAO RESPONSAVEL POR CHAMAR OUTRAS E DECIDIR ENTAO PARA ONDE O JOGO VAI'''
def menu():
    boasvindas()
    lista_jog =jogadores()
    nivel = qual_nivel()
    quant_tab = q_tabuleiro()
    term = como_para()
    
    if quant_tab=="1":
        jogo.tabunico(lista_jog, nivel,term)
    elif quant_tab=="2":
        jogo.tabduplo(lista_jog, nivel, term)
    return lista_jog
    


'''DA O START A CHAMADA DE FUNCOES E ENTAO INICIO DO JOGO'''
lista_jog =menu()


'''PERGUNTA SE DESEJA CONTINUAR A JOGAR'''
continuarjog=continua_nao()
while continuarjog =="1":
    lista_jog =menu()
    continuarjog=continua_nao()

'''PRINT FINAL, AO ENCERRAR O GAME'''
tabuleiros.separador()
print("\n\nObrigado por terem jogado!!!\n{}{}{} e {}{}{} voltem sempre!\n\n".format("\033[36m", lista_jog[0],"\033[0;0m","\033[31m", lista_jog[1],"\033[0;0m"))
tabuleiros.separador()