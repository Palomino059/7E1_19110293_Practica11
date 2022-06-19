import cv2

cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2() #Indicamos que vamos a utlilazar BackgraudoSubtractorMOG

while True:

    ret, frame = cap.read()
    if ret == False: break

    fgmask = fgbg.apply(frame) #aqui tenemos la primera mascara en blanco que representa el movimiento y el negro el fondo de la imagen

    cv2.imshow('fgmask', fgmask)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
