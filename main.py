# https://www.geeksforgeeks.org/python-using-pil-imagegrab-and-pytesseract/
# https://pyimagesearch.com/2020/05/25/tesseract-ocr-text-localization-and-detection/
# https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
# https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10
# https://favtutor.com/blogs/compare-strings-python
# https://www.youtube.com/watch?v=qIJpBz6R2Uw&ab_channel=Coding101withSteve
# https://www.journaldev.com/23763/python-remove-spaces-from-string#:~:text=Python%20String%20strip()%20function%20will%20remove%20leading%20and%20trailing%20whitespaces.&text=If%20you%20want%20to%20remove,or%20rstrip()%20function%20instead.
# https://appdividend.com/2022/03/22/how-to-print-type-of-variable-in-python/#:~:text=To%20print%20the%20type%20of,use%20the%20print()%20function
# https://www.datacamp.com/community/tutorials/mysql-python
# https://stackoverflow.com/questions/7536755/regular-expression-for-matching-hhmm-time-format
# https://mkaz.blog/code/python-string-format-cookbook/
# https://www.tutorialkart.com/python/python-round/python-round-to-nearest-10/#:~:text=Python%20%E2%80%93%20Round%20Number%20to%20Nearest,left%20of%20the%20decimal%20point.
# https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
# https://datagy.io/python-count-occurrences-in-list/#:~:text=The%20easiest%20way%20to%20count,in%20the%20list%20is%20returned.
# https://realpython.com/iterate-through-dictionary-python/#how-to-iterate-through-a-dictionary-in-python-the-basics
# import winsound
# import PIL
# import mysql.connector as sql
import numpy as nm
import numpy as np
import pyautogui as gui
import pytesseract as tesseract
import re
import cv2
import time
import ctypes
from pytesseract import Output
from PIL import ImageGrab

# Path of tesseract executable
tesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def contagem(tempo):
    while tempo > 0:
        # if tempo <= 10:
        #     # emite som de alerta com contagem regressiva de 10 segundos
        #     winsound.Beep(900, 100)
        print("Tempo restante: {0}s\r".format(tempo))
        tempo -= 1
        time.sleep(1)


def contagemSemPrint(tempo):
    print("Aguardando {}s".format(tempo))
    time.sleep(tempo)


def clique(x, y):
    # clica nas coordenadas que o botão está para dar foco na janela/fechar qualquer popup
    gui.click(x, y, duration=0.1)


def cliqueSleep(x, y, sleep):
    # clica nas coordenadas que o botão está para dar foco na janela/fechar qualquer popup
    gui.click(x, y, duration=0.1)
    time.sleep(sleep)


def tecla(tecla):
    gui.press(tecla)


def tecla(tecla, sleep):
    gui.press(tecla)
    time.sleep(sleep)


def PrintTelaInteira(x, y):
    # ImageGrab-To capture the screen image in a loop.
    # Bbox used to capture a specific area.
    return (ImageGrab.grab(bbox=(0, 0, x, y)))


def PrintTela(x1, y1, x2, y2):
    # ImageGrab-To capture the screen image in a loop.
    # Bbox used to capture a specific area.
    return (ImageGrab.grab(bbox=(x1, y1, x2, y2)))


def ExtrairTexto(captura):
    # Converted the image to monochrome for it to be easily
    # read by the OCR and obtained the output String.
    texto = tesseract.image_to_string(cv2.cvtColor(nm.array(captura), cv2.COLOR_BGR2GRAY), lang='por+eng')
    texto = texto.split('\n')

    textofinal = ""

    for linha in texto:
        if not linha.isspace() and len(linha) > 0:
            textofinal += linha

    return (textofinal)

def ExtrairTextoRgb(captura):
    # Converted the image to monochrome for it to be easily
    # read by the OCR and obtained the output String.
    texto = tesseract.image_to_string(captura, lang='por+eng')
    texto = texto.split('\n')

    textofinal = ""

    for linha in texto:
        if not linha.isspace() and len(linha) > 0:
            textofinal += linha

    return (textofinal)


def ExtrairTextoBgr(captura):
    # Converted the image to monochrome for it to be easily
    # read by the OCR and obtained the output String.
    texto = tesseract.image_to_string(captura, lang='por+eng')
    texto = texto.split('\n')

    textofinal = ""

    for linha in texto:
        if not linha.isspace() and len(linha) > 0:
            textofinal += linha

    return (textofinal)


def VerificarLogin(popupLogin):
    texto = ExtrairTexto(
        PrintTela(popupLogin[0],
                  popupLogin[1],
                  popupLogin[2],
                  popupLogin[3]
                  )
    )
    return ("Fazer Login" in texto)


def FazerLogin():
    # Clicar na caixa de senha
    cliqueSleep(500, 610, 0.25)

    # Clicar na conta do Avira PWM e esperar digitá-la
    cliqueSleep(636, 710, 2)

    # Clicar na caixa de senha novamente
    cliqueSleep(500, 610, 0.25)

    # Aperta Enter para fazer o login (para garantir caso o pwm nao saia da frente)
    tecla("enter", 0)


def DesenharRetanguloImg(img):
    dict = ExtrairDict(img)

    for i in range (0, len(dict["text"])):
        confiabilidade = int(float(dict["conf"][i]))
        x = dict["left"][i]
        y = dict["top"][i]
        w = dict["width"][i]
        h = dict["height"][i]
        # if confiabilidade > -2:
        cv2.rectangle(img,
                      (x, y),
                      (x + w, y + h),
                      (255, 255, 255),
                      1)
            # cv2.rectangle(img_copia,
            #               (x, y),
            #               (x+w, y+h),
            #               (255,255,255),
            #
    return img


def DesenharRetanguloCoordenadas(img, x, y, w, h):
    cv2.rectangle(img,
                  (x, y),
                  (x + w, y + h),
                  (0, 0, 0),
                  1)
    # cv2.rectangle(img_copia,
    #               (x, y),
    #               (x+w, y+h),
    #               (255,255,255),
    #
    return img


def AcharTextoImg(dict, img, texto):
    achou = False
    for i in range(0, len(dict["text"])):
        confiabilidade = int(float(dict["conf"][i]))
        x = dict["left"][i]
        y = dict["top"][i]
        w = dict["width"][i]
        h = dict["height"][i]
        text = dict["text"][i]

        if confiabilidade > 20:
            cv2.rectangle(img,
                          (x, y),
                          (x + w, y + h),
                          (0, 0, 0),
                          1)
            # cv2.rectangle(img_copia,
            #               (x, y),
            #               (x+w, y+h),
            #               (255,255,255),
            #               1)

        if texto[0].upper() in text.upper() and not achou:
            if len(texto) > 1:
                if (texto[1].upper() in text.upper()) or (texto[1].upper() in dict["text"][i + 1].upper()):
                    achou = True

                    # print("{0} - {1} ({2}, {3}, {4}, {5})".format(text + " " + dict["text"][i + 1],
                    #                                               confiabilidade,
                    #                                               x,
                    #                                               y,
                    #                                               x + w,
                    #                                               y + h)
                    #       )
            else:
                achou = True

                # print("{0} - {1} ({2}, {3}, {4}, {5})".format(text,
                #                                               confiabilidade,
                #                                               x,
                #                                               y,
                #                                               x + w,
                #                                               y + h)
                #       )
    return x, y, w, h, img, achou


def VerificarDentroRoleta(roleta):
    x = 0
    y = 0
    w = 0
    h = 0
    achoulocal = False

    texto = roleta.split(" ")

    print = PrintTela(14, 263, 521, 528)
    gray = imgtogray(print)
    limiar = LimiarizacaoOtsu(gray)
    # inverter as cores
    limiar = 255 - limiar

    dict = ExtrairDict(limiar)
    x, y, w, h, limiar, achoulocal = AcharTextoImg(dict, limiar, texto)

    return achoulocal


def MaximizarJogo():
    cliqueSleep(1270, 413, 1)
    cliqueSleep(1257, 361, 1)


def VerificarInatividade():
    texto = ExtrairTexto(PrintTela(583, 549, 813, 585))

    return "inatividade" in texto


def SairInatividade():
    cliqueSleep(691, 618, 3)

# Função para clicar no menu superior de roletas da Bet no hall de entrada
def VoltarRoulette():
    cliqueSleep(364, 330, 1.2)


def VoltarHallEntrada():
    cliqueSleep(1290, 225, 2)


def VerificarDesconexao():
    texto = ExtrairTexto(PrintTela(557, 548, 804, 585))

    return "desligado" in texto


def VoltarRoletaAoVivo():
    cliqueSleep(666, 615, 5)
    tecla('pagedown', 1)

    clique(177, 426)


def imgtorgb(img):
    rgb = cv2.cvtColor(nm.array(img), cv2.COLOR_BGR2RGB)
    return rgb


def imgtogray(img):
    gray = cv2.cvtColor(nm.array(img), cv2.COLOR_BGR2GRAY)
    return gray


def bgrtogray(bgr):
    gray = cv2.cvtColor(nm.array(bgr), cv2.COLOR_BGR2GRAY)
    return gray


def ExtrairDict(rgb):
    dict = tesseract.image_to_data(rgb, output_type=Output.DICT)
    return dict

def DesfoqueMediana(img):
    return cv2.medianBlur(img, 3)


def DesfoqueBilateral(img):
    return cv2.bilateralFilter(img, 15, 55, 45)


def ErosaoImg(img):
    return cv2.erode(img, np.ones((3,3), np.uint8))


def DilatarImg(img):
    return cv2.dilate(img, np.ones((3,3), np.uint8))


def AberturaImg(img):
    erosao = ErosaoImg(img)
    return cv2.dilate(erosao, np.ones((5,5), np.uint8))


def FechamentoImg(img):
    dilatar = DilatarImg(img)
    return cv2.erode(dilatar, np.ones((5,5), np.uint8))


def AmpliarImg(img, fator_de_ampliação):
    # cv2.INTER_NEAREST (vizinho mais próximo. mais rápido)
    # cv2.INTER_LINEAR (bilinear. padrão. boa para aumentar ou diminuir)
    # cv2.INTER_AREA (melhor para redução. para ampliar, é semelhante ao nearest)
    # cv2.INTER_CUBIC (2ª melhor para ampliação. matriz 4x4 de pixels vizinhos
    # cv2.INTER_LANCZOS4 (melhor para ampliação. matriz 8x8 pixels vizinhos
    return cv2.resize(img, None, fx=fator_de_ampliação, fy=fator_de_ampliação, interpolation=cv2.INTER_CUBIC)


def InverterImg(img):
    return 255 - img


def LimiarizacaoBasica(gray):
    limiar, img = cv2.threshold(gray, 195, 255, cv2.THRESH_BINARY)
    # print("- Limiar atual: {}".format(limiar))
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def LimiarizacaoResultados(gray, limiar):
    limiar, img = cv2.threshold(gray, limiar, 255, cv2.THRESH_BINARY)
    # print("- Limiar atual: {}".format(limiar))
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def LimiarizacaoOtsu(gray):
    limiar, img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # print("- Limiar Gaussiano: {}".format(limiar))
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def LimiarizacaoAdaptMedia(gray):
    img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def LimiarizacaoAdaptGauss(gray):
    img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 7)
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def AcharRoleta(roleta):
    texto = roleta.split(" ")
    # print(texto)

    achou = False

    cliqueSleep(458, 12, 0.5)

    gui.hotkey("ctrl", "f")
    gui.typewrite("bet365 Roulette")
    contagemSemPrint(1)

    gui.hotkey("ctrl", "f")
    gui.typewrite(roleta)

    if texto[1] == "Italiana":
        gui.press("enter")

    contagemSemPrint(1)
    gui.press("esc")
    contagemSemPrint(1)

    rodadas = 0

    while not achou:
        rodadas += 1
        print("Rodada atual: {}".format(rodadas))

        img = PrintTela(10, 426, 1290, 976)
        gray = imgtogray(img)
        limiar = LimiarizacaoBasica(gray)
        invert_limiar = 255 - limiar
        img_copia = invert_limiar.copy()

        roletas = ExtrairDict(img_copia)
        x, y, w, h, img_copia, achou = AcharTextoImg(roletas, img_copia, texto)
        if achou:
            clique(x + (w / 2), y + (h / 2) + 438)


def ExibirImagem(img):
    cv2.imshow("", img)
    cv2.waitKey()


def LimiarizarImagemCruaOtsu(img):
    img = LimiarizacaoOtsu(imgtogray(imgtorgb(img)))
    return img


def AnalisarTelegram(img):
    retorno = ""
    achou = False
    dict = ExtrairDict(img)

    while not achou:
        for i in range(1, 8):
            if i == 1:
                texto = ["GREN", "RESPEITA"]
                x, y, w, h, img, achou = AcharTextoImg(dict, img, texto)
                retorno = "G"
            elif i == 2 and not achou:
                texto = ["RED", "NEM"]
                x, y, w, h, img, achou = AcharTextoImg(dict, img, texto)
                retorno = "R"
            elif i == 3 and not achou:
                texto = ["MESA", "EM"]
                x, y, w, h, img, achou = AcharTextoImg(dict, img, texto)
                retorno = "A"
            elif i == 4 and not achou:
                texto = ["JOGADA", "CONFIRMADA"]
                x, y, w, h, img, achou = AcharTextoImg(dict, img, texto)
                retorno = "C"
            elif i == 5 and not achou:
                texto = ["MANIPULA"]
                x, y, w, h, img, achou = AcharTextoImg(dict, img, texto)
                retorno = "M"
            elif i == 6 and not achou:
                texto = ["TURBULENTO"]
                x, y, w, h, img, achou = AcharTextoImg(dict, img, texto)
                retorno = "T"
            elif not achou:
                retorno = "O"
                achou = True

    return retorno, img


def ExtrairHora(img):
    dict = ExtrairDict(img)
    padrao_hora = "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
    hora = ""

    for i in range (0, len(dict["text"])):
        confiabilidade = int(float(dict["conf"][i]))
        if confiabilidade > 20:
            texto = dict["text"][i]
            if re.match(padrao_hora, texto):
                x = dict["left"][i]
                y = dict["top"][i]
                w = dict["width"][i]
                h = dict["height"][i]
                cv2.rectangle(img,
                              (x, y),
                              (x + w, y + h),
                              (0, 0, 0),
                              1)
                hora = texto
    return hora


def ExtrairRoletaEmAnalise(img):
    dict = ExtrairDict(img)
    roleta = ""
    contador = 0
    achou = False


    for i in range(0, len(dict["text"])):
        confiabilidade = int(float(dict["conf"][i]))
        if confiabilidade > 40:
            if contador == 0:
                roleta += dict["text"][i] + " "
                contador += 1
            elif contador == 1:
                roleta += dict["text"][i]
                contador += 1
    for texto in roletas:
        if roleta.upper() in texto.upper():
            achou = True

    return roleta, achou


def CalcularProbabilidades(resultados, ultimo_resultado, hora):
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
    elif hora not in resultados[tamanho-1][5]:
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


def CalcularApostaInicial(banca, roleta):
    # arredondando a aposta inicial para os múltiplos da "moeda" padrão
    moeda_padrao = 2.5 # para a banca inicial de 1.3k, essa é a ficha que tem em 99% das mesas
    bet_inicial = 0.04 # 4% da banca para permitir um gale de 4x
    aposta_inicial = round(banca * bet_inicial / moeda_padrao) * moeda_padrao

    if "American".upper() in roleta.upper():
        zero = aposta_inicial * 0.1
    else:
        zero = aposta_inicial * 0.05

    return aposta_inicial, zero


def VerificarMoedasDaRoleta(roleta):
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


def CalcularMoedasParaAposta(aposta, lista_de_moedas):
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
        for j in range (0, len(lista_de_moedas)):
            moeda = lista_de_moedas[j]
            if moeda == resultado:
                if resultado != auxiliar:
                    auxiliar = resultado
                    if i == 0:
                        resultados_auxiliar = [
                            (j+1, resultados.count(auxiliar))
                        ]
                    else:
                        resultados_auxiliar.append(
                            (j+1, resultados.count(auxiliar))
                        )
        i += 1
    resultado_final = dict(resultados_auxiliar)
    return resultado_final


def VerificarEntradaTelegram(x1, y1, x2, y2):
    achou = False
    entradas_validas = ["pares",
                        "impares",
                        "ímpares",
                        "coluna",
                        "colunas",
                        "dúzia",
                        "duzia"]

    while not achou:
        texto = ExtrairTextoBgr(
            LimiarizarImagemCruaOtsu(
                PrintTela(x1, y1, x2, y2)
            )
        )

        for entrada in entradas_validas:
            if entrada.upper() in texto.upper():
                achou = True

    return texto

if __name__ == '__main__':
    # TODO:
    # (OK) analisar grupo e interpretar qual estágio da jogada está (em análise, confirmada, green, red)
    # (OK) criar alguma forma de registro dos resultados (bd, log, planilha)
    # (OK) criar função para calculo de probabilidade baseado nos resultados anteriores (igual na planilha do google)
    # - criar arquivo algo para configuração da estratégia (arquivo.cfg, etc)
    # (OK) capturar sinal
    # - analisar resultado da roleta depois que entrou para saber se saiu da fase de análise para jogada confirmada
    # --- lembrar de comparar se a jogada confirmada é a mesma da roleta que o bot entrou
    # (OK) calcular quais fichas precisam ser selecionadas para fazer jogada (50 e 50 nas colunas e 5 no 0)
    # - analisar se precisa de gale ou se foi green/red
    # (OK) criar listas com os números das dúzias, colunas, preto, vermelho, par e ímpar
    # (OK) ativar modo de preparar para jogada (quando a chance da próxima jogada for maior que 94,5%
    # -
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
               "Age Of The Gods",]
    mesa_quantum = [
               "Quantum Roulette Live",
               "Quantum Auto Roulette",
               "Greek Quantum Roulette",
               "Quantum Roulette Italiana",]
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

    # numeros pares =
    # numeros impares =
    # 1a coluna =
    # 2a coluna =
    # 3a coluna =
    # 1a duzia =
    # 2a duzia =
    # 3a duzia =

    # moedas_da_aposta = CalcularMoedasParaAposta(60, VerificarMoedasDaRoleta("greek"))
    #
    # for id_moeda, reps in moedas_da_aposta.items():
    #     print("Moeda {} (R$ {}) {}x em cada coluna/dúzia"
    #           .format(id_moeda, VerificarMoedasDaRoleta("greek")[id_moeda - 1], reps))

    contagem(3)

    # descobre a resolução do monitor principal. Para o segundo monitor, passar 78 e 79 como parametros.
    user32 = ctypes.windll.user32
    x = user32.GetSystemMetrics(0)
    y = user32.GetSystemMetrics(1)

    popupLogin = (417, 455, 913, 740)

    aposta_inicial = 0
    banca = 1300
    zero = 0

    achou = False
    modo_jogo = False
    ultimo_resultado = ""
    resultados = [[]]
    roleta = ""
    # AcharRoleta(roletas[2])
    # print(
    # 389, 449, 514, 592
    teste = LimiarizacaoOtsu(AmpliarImg(imgtogray(PrintTela(424, 490, 491, 537)), 3))
    ExibirImagem(DesenharRetanguloImg(teste))
    dicionario = ExtrairDict(teste)
    print(dicionario)
    for i in range(0, len(dicionario)):
        confianca = dicionario["conf"][i]
        x = dicionario["left"][i]
        y = dicionario["top"][i]
        w = dicionario["width"][i]
        h = dicionario["height"][i]
        texto = dicionario["text"][i]
        print("Texto: {}\nConfiança: {}".format(texto, confianca))

    # )
    # print(min(fichas_maioria, key=lambda x:abs(x - 17)))

    while modo_jogo:
        if VerificarLogin(popupLogin):
            cont = 0
            while VerificarLogin(popupLogin):
                if cont > 0:
                    gui.hotkey("ctrl", "shift", "r")
                    contagemSemPrint(5)
                FazerLogin()
                contagemSemPrint(10)
                cont += 1

            contagemSemPrint(10)

            while not VerificarDentroRoleta(roletas[2]):
                time.sleep(0.5)

            MaximizarJogo()
            VoltarHallEntrada()
            VoltarRoulette()

        elif VerificarInatividade():
            SairInatividade()
            VoltarRoulette()

        elif VerificarDesconexao():
            VoltarRoletaAoVivo()
            contagemSemPrint(5)

            while not VerificarDentroRoleta(roletas[2]):
                time.sleep(0.5)

            MaximizarJogo()
            VoltarHallEntrada()
            VoltarRoulette()

        if resultados != [[]]:
            for resultado in resultados:
                print("{} - {:.2%} -  {:.2%} -  {:.2%} -  {:.2%} - {}".format(
                    resultado[0],
                    resultado[1],
                    resultado[2],
                    resultado[3],
                    resultado[4],
                    resultado[5])
                )

        # cliqueSleep(1500, 940, 0.05)
        #
        # for i in range (1, 5):
        #     tecla("pagedown",0.05)

        hora = ExtrairHora(LimiarizarImagemCruaOtsu(PrintTela(1688, 913, 1826, 941)))
        print_telegram = LimiarizarImagemCruaOtsu(PrintTela(1366, 743, 1840, 951))
        ultimo_resultado, print_telegram = AnalisarTelegram(print_telegram)

        if "r".upper() in ultimo_resultado.upper():
            print("RED :(")

            if resultados == [[]]:
                resultados, modo_jogo = CalcularProbabilidades(resultados, ultimo_resultado, hora)
            elif hora not in resultados[len(resultados) - 1][5]:
                resultados, modo_jogo = CalcularProbabilidades(resultados, ultimo_resultado, hora)

        elif "g".upper() in ultimo_resultado.upper():
            print("GREEN!!")

            if resultados == [[]]:
                resultados, modo_jogo = CalcularProbabilidades(resultados, ultimo_resultado, hora)
            elif hora not in resultados[len(resultados)-1][5]:
                resultados, modo_jogo = CalcularProbabilidades(resultados, ultimo_resultado, hora)

        elif "a".upper() in ultimo_resultado.upper():

            if modo_jogo:
                print_telegram = LimiarizarImagemCruaOtsu(PrintTela(1526, 882, 1833, 912))
                auxiliar, achou = ExtrairRoletaEmAnalise(print_telegram)

                if auxiliar.upper() != roleta.upper():
                    print("MESA EM ANÁLISE")
                    print(auxiliar, achou)
                    roleta = auxiliar

                    if "prestige".upper() in roleta.upper() and banca < 2600:
                        pass
                    else:
                        if not VerificarDentroRoleta(roleta):
                            VoltarHallEntrada()
                            VoltarRoulette()
                            AcharRoleta(roleta)
                            while not VerificarDentroRoleta(roleta):
                                contagemSemPrint(1)
                        aposta_inicial, zero = CalcularApostaInicial(banca, roleta)

        elif "c".upper() in ultimo_resultado.upper():
            print("JOGADA CONFIRMADA")
            moedas_aposta_1 = CalcularMoedasParaAposta(aposta_inicial / 2,
                                                       VerificarMoedasDaRoleta(roleta))
            moedas_aposta_2 = CalcularMoedasParaAposta(aposta_inicial / 2,
                                                       VerificarMoedasDaRoleta(roleta))
            estrategia = VerificarEntradaTelegram(1411, 857, 1829, 904)

        elif "m".upper() in ultimo_resultado.upper():
            print("MESA MANIPULADA! FICAR ATENTO")

        elif "t".upper() in ultimo_resultado.upper():
            print("Mercado turbulento!!")

        elif "o".upper() in ultimo_resultado.upper():
            print("Mandaram mensagem manual")
