import cv2
from PIL import Image
img = cv2.imread("qrcode.jpg")
detect = cv2.QRCodeDetector()
data, vertices_array, binary_qrcode = detect.detectAndDecode(img)
if vertices_array is not None:
  print("QRCode data: ")
  print(data)
else:
  print("There was some error")
flag=input("Do you want Image of qrcode(yes/no): ")
if flag=="yes":
    im = Image.open("qrcode.jpg")
    im.show()