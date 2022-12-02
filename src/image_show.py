from src import image_analysis
import cv2


def drawRectangleImg(img):
    dict = image_analysis.extractDict(img)

    for i in range(0, len(dict["text"])):
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


def drawRectangleCoordinates(img, x, y, w, h):
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


def showImage(img):
    cv2.imshow("", img)
    cv2.waitKey()


