import cv2
# LOOPING VIDEO
video = cv2.VideoCapture(0)
a=0
while True:
    a+=1
    check , frame = video.read()


    face_cascade = cv2.CascadeClassifier("C://Users//lenovo//Desktop//OpenCV//haarcascade_frontalface_default.xml")
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img,(21,21),0)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imshow("capturing" ,frame)
    cv2.imshow("Gaussian Blur" , blur_img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(f"No of frames {a}")
video.release()
cv2.destroyAllWindows()