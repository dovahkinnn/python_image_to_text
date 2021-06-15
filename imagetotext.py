import cv2 
import pytesseract
import pyautogui
import time
from PIL import Image
import pyscreenshot as ImageGrab
import pyscreenshot as ImageGrab
import time

import pytesseract
import pyautogui
import time
import numpy
from PIL import Image
from PIL import Image
time.sleep(4)

pyautogui.screenshot('images/11112.png')
#Create an Image Object from an Image
image = cv2.imread('images/11112.png')

y=434
x=41
h=53
w=195
crop_image = image[y:y+h, x:x+w]
cv2.imwrite('images/bo.png',crop_image)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('images/bo.png', cv2.IMREAD_GRAYSCALE)  

thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
thresh = cv2.resize(thresh, (0,0), fx=2, fy=2)  # scale image 1.25X

detected_text = pytesseract.image_to_string(thresh, config = '--psm 11 --oem 3 -c tessedit_char_whitelist=0123456789/DPV')
print(detected_text)
a="P160000/160000"
if detected_text.find(a) != -1:
    print ("Found!")
else:
    print("Not found!") 