import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('input.jpg')

gray = cv2.cv2Color(image, cv2.COLOR_BGR2GRAY)

faces = face)cascade.detectMultiScale(gray, 1.1, 4)

print("Number of faces detected: ", len(faces))

for(x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('imshow', image)
cv2.waitKey()
