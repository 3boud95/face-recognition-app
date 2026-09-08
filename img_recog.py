import cv2
import numpy as np
import face_recognition

image = face_recognition.load_image_file('images/Tom Hollands.jfif')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

imageTest = face_recognition.load_image_file('images/Robert Downey Jr.jpg')
imageTest = cv2.cvtColor(imageTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(image)[0]
faceEnc = face_recognition.face_encodings(image)[0]

faceLocTest = face_recognition.face_locations(imageTest)[0]
faceEncTest = face_recognition.face_encodings(imageTest)[0]

cv2.rectangle(image, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
cv2.rectangle(imageTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

compFace = face_recognition.compare_faces([faceEnc], faceEncTest)
faceDist = face_recognition.face_distance([faceEnc], faceEncTest)

results = str(compFace) + " " + str(round(faceDist[0], 2))

cv2.putText(image, results, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Image', image)
cv2.imshow('Image Test', imageTest)
cv2.waitKey(0)