import re

A = 0
B = 0
C = 0 
D = 0 

lista = []

def Norma(arquivo):
    #abrir arquivo e criar lista com os valores dos registradores e com as instruções#
    global A ,B, C, D, lista
    with open(arquivo, "r") as arq:
        lista = arq.readlines()
    ValorRegistrador(lista[0])
    return lerInstrucao(lista[1], True)
        

def lerInstrucao(linha, continua):
    #função que lê as instruções e as executa#
    global A ,B, C, D, lista

    if continua is False:
        return 1 

    pattern = re.compile(r'([0-9]+):([A-Z]{3}) ([A-Z]) ([0-9]+)\s?([0-9]+)?')
    #separa a instrução em partes e a salva em uma matriz.
    matches = pattern.findall(linha)


    instrucao = matches[0][1] #QUAL INSTRUÇÃO ?
    registrador = matches[0][2] #QUAL REGISTRADOR ?
    pularPara = int(matches[0][3]) #PULAR PARA QUAL FUNÇÃO ?
    if matches[0][4]:
        condPulo = int(matches[0][4]) #PULO deCONDICIONAL

    #CHECAR QUAL É A INSTRUÇÃO !!!
    if instrucao == "ADD":
        INC(registrador)
        return lerInstrucao(lista[pularPara], True)
    elif instrucao == "SUB":
        DEC(registrador)

        return lerInstrucao(lista[pularPara], True)
    elif instrucao == "ZER":
        if ZER(registrador):
            if pularPara == 404:#IF PARA O FINALIZAR O PROGRAMA !!!
                printInstrucao("O Resultado é: ", " ", True)
                return lerInstrucao(lista[0], False)
            return lerInstrucao(lista[pularPara], True)
        else:
            return lerInstrucao(lista[condPulo], True)
    
    
    
#FUNÇÃO QUE CHECA SE O REGISTRADOR É ZERO
def ZER(registrador): 
    global A ,B, C, D 
    if registrador == "A" and A == 0:
        return True
    elif registrador == "B" and B == 0:
        return True
    elif registrador == "C" and C == 0:
        return True
    elif registrador == "D" and D == 0:
        return True
    return False

#FUNÇÃO INCREMENTADORA
def INC(registrador):
    global A ,B, C, D 
    if registrador == "A":
            A += 1
            printInstrucao("SOMA:", " Reg_1")
    elif registrador == "B":
            B += 1
            printInstrucao("SOMA:", " Reg_2")
    elif registrador == "C":
            C += 1
            printInstrucao("SOMA:", " Reg_3")
    else:
            D += 1
            printInstrucao("SOMA:", " Reg_4")
    
#FUNÇÃO DECREMENTADORA
def DEC(registrador):
    global A ,B, C, D 
    if registrador == "A":
            A -= 1
            printInstrucao("SUBTRAI:", " Reg_1")
    elif registrador == "B":
            B -= 1
            printInstrucao("SUBTRAI:", " Reg_2")
    elif registrador == "C":
            C -= 1
            printInstrucao("SUBTRAI:", " Reg_3")
    else:
            D -= 1
            printInstrucao("SUBTRAI:", " Reg_4")
    
#DEFINIR VALOR DOS REGISTRADORES
def ValorRegistrador(linha):
    global A ,B, C, D
    pattern = re.compile(r'([0-9]+)')
    matches = pattern.findall(linha)
    A = int(matches[0])

    B = int(matches[1])

    C = int(matches[2])

    D = int(matches[3])

    printInstrucao("INICIALIZA:")



#IMPRIME EM QUE INSTRUÇÃO ESTA E O QUE ELA FEZ.
def printInstrucao(linha, reg = " Reg_1 e Reg_2", final = False):
    if final == False:
        print(str(linha) + str(reg) + " - " + "(R_1: " + str(A) + ", R_2: " + str(B) + ", R_3: " + str(C) + ", R_4: " + str(D) + ")" )
    else:
        print(str(linha) + "(" + str(C) + ", " + str(A) + ")")