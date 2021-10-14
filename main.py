#convert text to QR code
import qrcode
img = qrcode.make("I love coding")
img.save("code.jpg")

#QR code to text
import cv2
a= cv2.QRCodeDetector()
val, _, _=a.detectAndDecode(cv2.imread("code.jpg"))
print('Decoded text: ',val)