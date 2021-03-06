import cv2
from imutils import resize


frontalFaceClassifier = cv2.CascadeClassifier(f'classifier/haarcascade_frontalface_default.xml')
mouthClassifier = cv2.CascadeClassifier(f'classifier/haarcascade_mcs_mouth.xml')
noseClassifier = cv2.CascadeClassifier(f'classifier/haarcascade_mcs_nose.xml')

def analysisImg(img):
    face = cv2.imread(img)

    height, width, _ = face.shape
    if height>700 or width>700:
        face = resize(face, width=700)
    
    grayImg = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    faces = frontalFaceClassifier.detectMultiScale(grayImg, 1.1, 3)
    
    for (x, y, l, a) in faces:
        cropImg = grayImg[y:y+a, x:x+l]
        mouth = mouthClassifier.detectMultiScale(cropImg, 1.1, 5)
        nose = noseClassifier.detectMultiScale(cropImg, 1.1, 5)
        if len(mouth) > 0 and len(nose) > 0:
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
            cv2.destroyAllWindows()
            break

        cv2.imshow('Camera | Press ESC to stop', frame)