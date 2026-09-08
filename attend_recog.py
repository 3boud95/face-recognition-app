import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = "attendance images"
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    img = cv2.imread(f"{path}/{cl}")
    classNames.append(os.path.splitext(cl)[0])
    images.append(img)
print(classNames)

def findEncodings(images):
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendace(name):
    with open('attendance.csv', 'r+') as f:
        dataList = f.readlines()
        nameList = []
        for line in dataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            stamp = datetime.now()
            dtString = stamp.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

knownEncodings = findEncodings(images)
print("Encoding Complete")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    locCurr = face_recognition.face_locations(imgS)
    encodeCurr = face_recognition.face_encodings(imgS, locCurr)

    for encode, loc in zip(encodeCurr, locCurr):
        matches = face_recognition.compare_faces(knownEncodings, encode)
        faceDis = face_recognition.face_distance(knownEncodings, encode)
        right = np.argmin(faceDis)

        if matches[right]:
            name = classNames[right].upper()
            # print(name)
            y1, x2, y2, x1 = loc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendace(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)

