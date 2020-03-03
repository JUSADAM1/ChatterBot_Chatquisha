# imported opencv cause they have the facial REC feature.
import cv2 as cv

def face_rec():

    cap = cv.VideoCapture(0)

    face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv.CASCADE_SCALE_IMAGE
            )

            num_faces = len(faces)
            print("Found {0} faces!".format(num_faces))

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv.imshow("Setup", frame)

            if cv.waitKey(1) == ord('p') & 0xFF:
                name = input("Please enter your name: ")
                cv.imwrite(name + ".jpg", frame)
                break

    # When everyth1ing done, release the capture
    cap.release()
    cv.destroyAllWindows()
# Tiding it together with the others

if __name__ == '__main__':
    face_rec()