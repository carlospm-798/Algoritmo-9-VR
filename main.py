#Algoritmo 9
#Carlos Paredes Márquez
#27 09 2021

import cv2

im = cv2.imread('perro.jpg')

im_fondo = cv2.imread('yo.jpeg')
h,w,_ = im.shape
im_fondo = cv2.resize(im_fondo, (w,h))

hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
mask0 = cv2.inRange(hsv, (55, 0, 0), (65, 255, 255))
mask = cv2.bitwise_not(mask0)
im2 = cv2.bitwise_and(im, im, mask=mask)

im3 = cv2.bitwise_and(im_fondo, im_fondo, mask=mask0)
im4 = cv2.bitwise_or(im3, im2)


cv2.imshow('final_image',im4)
cv2.waitKey(0)