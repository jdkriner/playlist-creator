import cv2
import pytesseract
import re 
#img = cv2.imread('rollingloud2021.jpg')
#text = pytesseract.image_to_string(img)
#print(text)
image = cv2.imread('rollingloud2021.jpg') #loads theimage to be used

#image processing to make it more readable
blownup = cv2.resize(image, (0, 0), fx = 2, fy = 2)
greyscale = cv2.cvtColor(blownup, cv2.COLOR_BGR2GRAY) 
clearimg = cv2.GaussianBlur(greyscale, [0, 0], 1)
finalimg = cv2.threshold(clearimg, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#image processing pt2
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
#opening = cv2.morphologyEx(finalimg, cv2.MORPH_OPEN, kernel, iterations=1)
#invert = 255 - opening


#read text
text = pytesseract.image_to_string(finalimg, lang='eng', config='--psm 4')
print(text)

cv2.imshow('grey', greyscale)
cv2.imshow('clear', clearimg)
cv2.imshow('final', finalimg)

cv2.waitKey()
#12, 11, 4 the best

