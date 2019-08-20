import cv2
# FACE DETECTION

img = cv2.imread("C://Users//lenovo//Desktop//OpenCV//faces.png", 1)
face_cascade = cv2.CascadeClassifier("C://Users//lenovo//Desktop//OpenCV//haarcascade_frontalface_default.xml")
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05 , minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img , (x,y) , (x+w , y+h) , (0,0,255) , 3)



img = cv2.resize( img , (1200,800) )

cv2.imshow("img" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()