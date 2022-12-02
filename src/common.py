import ctypes
import time

roletas = ["American Roulette",
           "Auto Roulette",
           "bet365 Roulette",
           "bet365 Dutch Roulette",
           "Roleta Brasileira",
           "Deutsches Roulette",
           "Football Roulette",
           "Age Of The Gods",
           "Greek Roulette",
           "Hindi Roulette",
           "Roulette Italiana",
           "Mega Fire Blaze Roulette Live",
           "Who Wants To Be a Millionaire",
           "Prestige Roulette",
           "Quantum Roulette Live",
           "Quantum Auto Roulette",
           "Greek Quantum Roulette",
           "Quantum Roulette Italiana",
           "French Roulette",
           "Speed Roulette",
           "Speed Auto Roulette",
           "Spread Bet Roulette",
           "Super Spin Roulette",
           "Triumph Roulette",
           "Turkish Roulette",
           "UK Roulette"]
mesa_maioria = ["American Roulette",
                "Auto Roulette",
                "bet365 Roulette",
                "bet365 Dutch Roulette",
                "Roleta Brasileira",
                "Deutsches Roulette",
                "Greek Roulette",
                "Hindi Roulette",
                "Roulette Italiana",
                "Who Wants To Be a Millionaire",
                "Prestige Roulette",
                "Speed Roulette",
                "Speed Auto Roulette",
                "Spread Bet Roulette",
                "Triumph Roulette",
                "Turkish Roulette",
                "UK Roulette"]
mesa_gods = [
    "Football Roulette",
    "Age Of The Gods", ]
mesa_quantum = [
    "Quantum Roulette Live",
    "Quantum Auto Roulette",
    "Greek Quantum Roulette",
    "Quantum Roulette Italiana", ]
roletas_um = ["American Roulette",
              "Quantum Roulette Live",
              "Quantum Auto Roulette",
              "Greek Quantum Roulette",
              "Quantum Roulette Italiana",
              "Super Spin Roulette",
              "Mega Fire Blaze Roulette Live",
              "Who Wants To Be a Millionaire",
              "Age Of The Gods"
              ]
roletas_maioria = ["Auto Roulette",
                   "bet365 Roulette",
                   "bet365 Dutch Roulette",
                   "Roleta Brasileira",
                   "Deutsches Roulette",
                   "Football Roulette",
                   "Greek Roulette",
                   "Hindi Roulette",
                   "Roulette Italiana",
                   "French Roulette",
                   "Speed Roulette",
                   "Speed Auto Roulette",
                   "Spread Bet Roulette",
                   "Triumph Roulette",
                   "Turkish Roulette",
                   "UK Roulette"
                   ]
roletas_cinco = [
    "Prestige Roulette"
]

fichas_um = [1, 2.5, 5, 20, 50, 100]
fichas_maioria = [2.5, 5, 25, 50, 125, 500]
fichas_cinco = [5, 25, 50, 125, 500, 2500]

vermelhos = [1, 3, 5, 7, 9, 12, 15, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
pretos = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
num_baixos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
num_altos = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
duzia_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
duzia_2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
duzia_3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
coluna_1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
coluna_2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
coluna_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]


def getScreenResolution():
    user32 = ctypes.windll.user32
    x = user32.GetSystemMetrics(0)
    y = user32.GetSystemMetrics(1)

    return x, y


def countdown(tempo):
    while tempo > 0:
        # if tempo <= 10:
        #     # emite som de alerta com contagem regressiva de 10 segundos
        #     winsound.Beep(900, 100)
        print("Tempo restante: {0}s\r".format(tempo))
        tempo -= 1
        time.sleep(1)


def printlessCountdown(tempo):
    print("Aguardando {}s".format(tempo))
    time.sleep(tempo)


def calculateOdds(resultados, ultimo_resultado, hora):
    chance_green_geral = 0.964
    chance_red_geral = 1 - chance_green_geral
    minimo_de_chance = 0.945
    resultado = []
    tamanho = len(resultados)

    if resultados == [[]]:
        resultado = [ultimo_resultado,
                     chance_green_geral,
                     chance_red_geral,
                     chance_green_geral * chance_green_geral,
                     1 - (chance_green_geral * chance_green_geral),
                     hora]
        resultados = [resultado]
    elif hora not in resultados[tamanho - 1][5]:
        resultado.append(ultimo_resultado)
        # =IF(ISBLANK(A4);"";IF(B3="G";I3;1-H4))
        # =IF(ISBLANK(A4);"";IF(B3="G";J3;H3*$H$2))
        if "G".upper() in resultados[tamanho - 1][0].upper():
            resultado.append(resultados[tamanho - 1][3])
            resultado.append(resultados[tamanho - 1][4])
        else:
            resultado.append(1 - (resultados[tamanho - 1][2] * chance_red_geral))
            resultado.append(resultados[tamanho - 1][2] * chance_red_geral)
        # =IF(ISBLANK(A4);"";IF(B4="G";G4*$G$2;1-J4))
        # =IF(ISBLANK(A4);"";IF(B4="G";1-I4;H4*$H$2))
        if "G".upper() in ultimo_resultado:
            resultado.append(resultado[1] * chance_green_geral)
            resultado.append(1 - (resultado[1] * chance_green_geral))
        else:
            resultado.append(1 - (resultado[2] * chance_red_geral))
            resultado.append(resultado[2] * chance_red_geral)
        resultado.append(hora)
        resultados.append(resultado)

    return resultados, resultado[3] >= minimo_de_chance


def calculateInitialBet(banca, roleta):
    # arredondando a aposta inicial para os múltiplos da "moeda" padrão
    moeda_padrao = 2.5  # para a banca inicial de 1.3k, essa é a ficha que tem em 99% das mesas
    bet_inicial = 0.04  # 4% da banca para permitir um gale de 4x
    aposta_inicial = round(banca * bet_inicial / moeda_padrao) * moeda_padrao

    if "American".upper() in roleta.upper():
        zero = aposta_inicial * 0.1
    else:
        zero = aposta_inicial * 0.05

    return aposta_inicial, zero


def verifyRouletteCoins(roleta):
    achou = False
    retorno = []

    for nome in roletas_cinco:
        if roleta.upper() in nome.upper():
            achou = True
            retorno = fichas_cinco

    if not achou:
        for nome in roletas_um:
            if roleta.upper() in nome.upper():
                achou = True
                retorno = fichas_um
        if not achou:
            retorno = fichas_maioria

    return retorno


def calculateBetCoins(aposta, lista_de_moedas):
    auxiliar = 0
    i = 1
    resultados = []
    resultados_auxiliar = []

    while aposta >= lista_de_moedas[0] and i <= len(lista_de_moedas):
        if aposta >= lista_de_moedas[len(lista_de_moedas) - i]:
            aposta = aposta - lista_de_moedas[len(lista_de_moedas) - i]
            resultados.append(lista_de_moedas[len(lista_de_moedas) - i])
        else:
            i += 1
    i = 0
    for resultado in resultados:
        for j in range(0, len(lista_de_moedas)):
            moeda = lista_de_moedas[j]
            if moeda == resultado:
                if resultado != auxiliar:
                    auxiliar = resultado
                    if i == 0:
                        resultados_auxiliar = [
                            (j + 1, resultados.count(auxiliar))
                        ]
                    else:
                        resultados_auxiliar.append(
                            (j + 1, resultados.count(auxiliar))
                        )
        i += 1
    resultado_final = dict(resultados_auxiliar)
    return resultado_final
