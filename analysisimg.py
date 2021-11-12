import cv2


HAARCASCADE = 'haarcascade_'
XML = '.xml'

frontalFaceClassifier = cv2.CascadeClassifier(f'classifier/{HAARCASCADE}frontalface_default{XML}')
mouthClassifier = cv2.CascadeClassifier(f'classifier/{HAARCASCADE}mcs_mouth{XML}')
noseClassifier = cv2.CascadeClassifier(f'classifier/{HAARCASCADE}mcs_nose{XML}')

def analysisImg(img):
    face = cv2.imread(f'img/{img}')
    grayImg = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    faces = frontalFaceClassifier.detectMultiScale(grayImg, 1.1, 3)
    
    for (x, y, l, a) in faces:
        cropImg = grayImg[y:y+a, x:x+l]
        mouth = mouthClassifier.detectMultiScale(cropImg, 1.1, 5)
        nose = noseClassifier.detectMultiScale(cropImg, 1.1, 5)
        if len(mouth) > 0:
            cv2.putText(face, "Sem Mascara", (x,y-10), 2, 0.5, (0, 0, 255))
            cv2.rectangle(face, (x, y), (x+l, y+a), (0, 0, 255), 2)

    cv2.imshow('img', face)
    cv2.waitKey(0)

def analysisWebCam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = frontalFaceClassifier.detectMultiScale(grayImg, 1.1, 3)

        for (x, y, l, a) in faces:
            cropImg = grayImg[y:y+a, x:x+l]
            mouth = mouthClassifier.detectMultiScale(cropImg, 1.1, 5)
            nose = noseClassifier.detectMultiScale(cropImg, 1.1, 5)
            if len(mouth) > 0 and len(nose) > 0:
                cv2.putText(frame, "SEM MASCARA", (x,y), 2, 0.5, (0, 0, 255))
                cv2.rectangle(frame, (x, y+10), (x+l, y+a), (0, 0, 255), 2)

        c = cv2.waitKey(1)
        if c == 27:
            break

        cv2.imshow('Camera', frame)