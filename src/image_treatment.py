import cv2
import numpy as np


def medianBlur(img):
    return cv2.medianBlur(img, 3)


def bilateralBlur(img):
    return cv2.bilateralFilter(img, 15, 55, 45)


def erodeImg(img):
    return cv2.erode(img, np.ones((3, 3), np.uint8))


def dilateImg(img):
    return cv2.dilate(img, np.ones((3, 3), np.uint8))


def openingImg(img):
    erosao = erodeImg(img)
    return cv2.dilate(erosao, np.ones((5, 5), np.uint8))


def closingImg(img):
    dilatar = dilateImg(img)
    return cv2.erode(dilatar, np.ones((5, 5), np.uint8))


def expandImg(img, fator_de_ampliação):
    # cv2.INTER_NEAREST (vizinho mais próximo. mais rápido)
    # cv2.INTER_LINEAR (bilinear. padrão. boa para aumentar ou diminuir)
    # cv2.INTER_AREA (melhor para redução. para ampliar, é semelhante ao nearest)
    # cv2.INTER_CUBIC (2ª melhor para ampliação. matriz 4x4 de pixels vizinhos
    # cv2.INTER_LANCZOS4 (melhor para ampliação. matriz 8x8 pixels vizinhos
    return cv2.resize(img, None, fx=fator_de_ampliação, fy=fator_de_ampliação, interpolation=cv2.INTER_CUBIC)


def invertImg(img):
    return 255 - img


def rawImgOtsuLimiarization(img):
    img = otsuLimiarization(imgToGray(imgToRgb(img)))
    return img


def basicLimiarization(gray):
    limiar, img = cv2.threshold(gray, 195, 255, cv2.THRESH_BINARY)
    # print("- Limiar atual: {}".format(limiar))
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def resultsLimiarization(gray, limiar):
    limiar, img = cv2.threshold(gray, limiar, 255, cv2.THRESH_BINARY)
    # print("- Limiar atual: {}".format(limiar))
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def otsuLimiarization(gray):
    limiar, img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # print("- Limiar Gaussiano: {}".format(limiar))
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def mediumAdaptLimiarization(gray):
    img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def gaussAdaptLimiarization(gray):
    img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 7)
    # cv2.imshow("Limiarizacao Simples", limiar)
    # cv2.waitKey()

    return img


def imgToRgb(img):
    rgb = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    return rgb


def imgToGray(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    return gray


def bgrToGray(bgr):
    gray = cv2.cvtColor(np.array(bgr), cv2.COLOR_BGR2GRAY)
    return gray
