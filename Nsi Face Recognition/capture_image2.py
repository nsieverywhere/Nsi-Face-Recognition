import numpy as np
import os
import cv2
import pickle
# create a folder for storing the image captured

# import tolet as t
# print(t.at.ew())


def capture(path):

    face_cascade = cv2.CascadeClassifier(
        'cascades/data/haarcascade_frontalface_alt2.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")
    cap = cv2.VideoCapture(0)

    def takephoto():
        c = [1, 2, 3, 4]
        for a in c:

            # print('you clicked' + nb)
            while a <= 100:
                ret, frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(
                    gray, scaleFactor=1.2, minNeighbors=5)
                for (x, y, w, h) in faces:
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = frame[y:y+h, x:x+w]
                    id_, conf = recognizer.predict(roi_gray)
                    # ret, frame = cap.read()
                    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    # faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
                    if conf >= 45 and conf <= 85:
                        print(id)
                    color = (255, 0, 0)
                    stroke = 2
                    end_cord_x = x + w
                    end_cord_y = y + h
                    cv2.rectangle(frame, (x, y), (end_cord_x,
                                                  end_cord_y), color, stroke)

                cv2.imshow('frame', frame)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                cv2.imwrite(path + '/%s.png' % a, gray)
                a = a+1

            break

    takephoto()

    cv2.destroyAllWindows()
    cap.release()
