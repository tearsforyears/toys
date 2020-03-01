import cv2

cap = cv2.VideoCapture(0)
SEC = 1000
FPS = 50
FEQ = int(SEC / FPS)
PATH = r"./haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(PATH)
while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3, minSize=(30, 30), )
    for (x, y, width, height) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    cv2.imshow('', frame)
    if cv2.waitKey(FEQ) != -1:
        break
    try:
        pass
    except Exception:
        break
cap.release()
