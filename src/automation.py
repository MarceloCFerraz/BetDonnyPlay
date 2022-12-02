import pyautogui as gui
from src import common, image_capture, image_treatment, image_analysis
import time


def updatePage():
    gui.hotkey("ctrl", "shift", "r")


def click(x, y):
    # clica nas coordenadas que o botão está para dar foco na janela/fechar qualquer popup
    gui.click(x, y, duration=0.1)


def clickSleep(x, y, sleep):
    # clica nas coordenadas que o botão está para dar foco na janela/fechar qualquer popup
    gui.click(x, y, duration=0.1)
    time.sleep(sleep)


def pressKey(tecla):
    gui.press(tecla)


def pressKey(tecla, sleep):
    gui.press(tecla)
    time.sleep(sleep)


def login():
    # Clicar na caixa de senha
    clickSleep(500, 610, 0.25)

    # Clicar na conta do Avira PWM e esperar digitá-la
    clickSleep(636, 710, 2)

    # Clicar na caixa de senha novamente
    clickSleep(500, 610, 0.25)

    # Aperta Enter para fazer o login (para garantir caso o pwm nao saia da frente)
    pressKey("enter", 0)


def maximizeGame():
    clickSleep(1270, 413, 1)
    clickSleep(1257, 361, 1)


def closeInactivity():
    clickSleep(691, 618, 3)


# Função para clicar no menu superior de roletas da Bet no hall de entrada
def openRoulettesMenu():
    clickSleep(364, 330, 1.2)


def getBackAtHall():
    clickSleep(1290, 225, 2)


def getBackAtLiveRoulette():
    clickSleep(666, 615, 5)
    pressKey('pagedown', 1)

    click(177, 426)


def findRoulette(roleta):
    texto = roleta.split(" ")
    # print(texto)

    achou = False

    clickSleep(458, 12, 0.5)

    gui.hotkey("ctrl", "f")
    gui.typewrite("bet365 Roulette")
    common.printlessCountdown(1)

    gui.hotkey("ctrl", "f")
    gui.typewrite(roleta)

    if texto[1] == "Italiana":
        gui.press("enter")

    common.printlessCountdown(1)
    gui.press("esc")
    common.printlessCountdown(1)

    rodadas = 0

    while not achou:
        rodadas += 1
        print("Rodada atual: {}".format(rodadas))

        img = image_capture.printScreen(10, 426, 1290, 976)
        gray = image_treatment.imgToGray(img)
        limiar = image_treatment.basicLimiarization(gray)
        invert_limiar = 255 - limiar
        img_copia = invert_limiar.copy()

        roletas = image_analysis.extractDict(img_copia)
        x, y, w, h, img_copia, achou = image_analysis.findTextOnImg(roletas, img_copia, texto)
        if achou:
            click(x + (w / 2), y + (h / 2) + 438)
