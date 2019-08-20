import cv2 , time

#
# video = cv2.VideoCapture(0)
#
# check ,frame = video.read()
#
# print(check)
# print(frame)
#
# time.sleep(1)
#
# cv2.imshow("Capturing" , frame)
# cv2.waitKey(0)
#
# video.release()
# cv2.destroyAllWindows()


# LOOPING VIDEO
video = cv2.VideoCapture(0)
a=0
while True:
    a+=1
    check , frame = video.read()
    # gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier("C://Users//lenovo//Desktop//OpenCV//haarcascade_frontalface_default.xml")
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imshow("capturing" ,frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(f"No of frames {a}")
video.release()
cv2.destroyAllWindows()