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
from src import common, automation, image_analysis, image_capture, image_treatment, image_show
import pytesseract as tesseract
import time

# Path of tesseract executable
tesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

if __name__ == '__main__':

    common.countdown(3)

    # descobre a resolução do monitor principal. Para o segundo monitor, passar 78 e 79 como parametros.
    x, y = common.getScreenResolution()

    popupLogin = (417, 455, 913, 740)

    aposta_inicial = 0
    banca = 1300
    zero = 0

    achou = False
    modo_jogo = False
    ultimo_resultado = ""
    resultados = [[]]
    roleta = ""
    teste = image_treatment.otsuLimiarization(
        image_treatment.expandImg(
            image_treatment.imgToGray(
                image_capture.printScreen(424, 490, 491, 537)
            )
            , 3
        )
    )
    image_show.showImage(image_show.drawRectangleImg(teste))
    dicionario = image_analysis.extractDict(teste)
    print(dicionario)
    for i in range(0, len(dicionario)):
        confianca = dicionario["conf"][i]
        x = dicionario["left"][i]
        y = dicionario["top"][i]
        w = dicionario["width"][i]
        h = dicionario["height"][i]
        texto = dicionario["text"][i]
        print("Texto: {}\nConfiança: {}".format(texto, confianca))

    while modo_jogo:
        if image_analysis.verifyLogin(popupLogin):
            cont = 0
            while image_analysis.verifyLogin(popupLogin):
                if cont > 0:
                    automation.updatePage()
                    common.printlessCountdown(5)
                automation.login()
                common.printlessCountdown(10)
                cont += 1

            common.printlessCountdown(10)

            while not image_analysis.verifyInRoulette(common.roletas[2]):
                time.sleep(0.5)

            automation.maximizeGame()
            automation.getBackAtHall()
            automation.openRoulettesMenu()

        elif image_analysis.verifyInactivity():
            automation.closeInactivity()
            automation.openRoulettesMenu()

        elif image_analysis.verifyDisconnection():
            automation.getBackAtLiveRoulette()
            common.printlessCountdown(5)

            while not image_analysis.verifyInRoulette(common.roletas[2]):
                time.sleep(0.5)

            automation.maximizeGame()
            automation.getBackAtHall()
            automation.openRoulettesMenu()

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

        hora = image_analysis.extractHour(
            image_treatment.rawImgOtsuLimiarization(image_capture.printScreen(1688, 913, 1826, 941)))
        print_telegram = image_treatment.rawImgOtsuLimiarization(image_capture.printScreen(1366, 743, 1840, 951))
        ultimo_resultado, print_telegram = image_analysis.analyseTelegram(print_telegram)

        if "r".upper() in ultimo_resultado.upper():
            print("RED :(")

            if resultados == [[]]:
                resultados, modo_jogo = common.calculateOdds(resultados, ultimo_resultado, hora)
            elif hora not in resultados[len(resultados) - 1][5]:
                resultados, modo_jogo = common.calculateOdds(resultados, ultimo_resultado, hora)

        elif "g".upper() in ultimo_resultado.upper():
            print("GREEN!!")

            if resultados == [[]]:
                resultados, modo_jogo = common.calculateOdds(resultados, ultimo_resultado, hora)
            elif hora not in resultados[len(resultados)-1][5]:
                resultados, modo_jogo = common.calculateOdds(resultados, ultimo_resultado, hora)

        elif "a".upper() in ultimo_resultado.upper():

            if modo_jogo:
                print_telegram = image_treatment.rawImgOtsuLimiarization(
                    image_capture.printScreen(1526, 882, 1833, 912))
                auxiliar, achou = image_analysis.extractAnalysisRoulette(print_telegram)

                if auxiliar.upper() != roleta.upper():
                    print("MESA EM ANÁLISE")
                    print(auxiliar, achou)
                    roleta = auxiliar

                    if "prestige".upper() in roleta.upper() and banca < 2600:
                        pass
                    else:
                        if not image_analysis.verifyInRoulette(roleta):
                            automation.getBackAtHall()
                            automation.openRoulettesMenu()
                            automation.findRoulette(roleta)
                            while not image_analysis.verifyInRoulette(roleta):
                                common.printlessCountdown(1)
                        aposta_inicial, zero = common.calculateInitialBet(banca, roleta)

        elif "c".upper() in ultimo_resultado.upper():
            print("JOGADA CONFIRMADA")
            moedas_aposta_1 = common.calculateBetCoins(
                aposta_inicial / 2,
                common.verifyRouletteCoins(roleta)
            )
            moedas_aposta_2 = common.calculateBetCoins(
                aposta_inicial / 2,
                common.verifyRouletteCoins(roleta)
            )
            estrategia = image_analysis.verifyTelegramInput(1411, 857, 1829, 904)

        elif "m".upper() in ultimo_resultado.upper():
            print("MESA MANIPULADA! FICAR ATENTO")

        elif "t".upper() in ultimo_resultado.upper():
            print("Mercado turbulento!!")

        elif "o".upper() in ultimo_resultado.upper():
            print("Mandaram mensagem manual")
