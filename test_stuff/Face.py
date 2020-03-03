import cv2
import face_recognition
import numpy as np
import dlib

# vid = cv2.VideoCapture(0)
# # Creating Variable
# a = 0
# a = a + 1
# # Creating a frame object to read photo
# check, frame = vid.read()
# # show the frame
# cv2.imshow("Capturing", frame)
# # For playing
# key = cv2.waitKey(1)
# # This is for saving the image
# showPic = cv2.imwrite("MAD_justyn.jpg", frame)
# print(showPic)
#
# vid.release()
# cv2.destroyAllWindows()

# Camera
vid_capture = cv2.VideoCapture(0)

# BUT IN THIS CASE EMOTIONS
# Loads the test picture so it can learn how to recognize the person
Happy_image = face_recognition.load_image_file("Photo.jpg")
Happy_face_encoding = face_recognition.face_encodings(Happy_image)[0]

# Loads the test picture so it can learn how to recognize the person


# Creating an array of data we have
ppl_we_know_encoding = [
    Happy_face_encoding,

]
# Adding names to the data collected or given
ppl_we_know_names = [
    "Photo.jpg"
]
# To initialize some VARS
face_location = []
face_encodings = []
face_names = []

To_process_frames = True

while True:
    # To Grab single frames from the video captured on cam
    ret, frame = vid_capture.read()

    # To resize the vid
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    if To_process_frames:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Check if we got any matches
            matches = face_recognition.compare_faces(ppl_we_know_encoding, face_encoding)
            name = "UNKNOWN"

            face_distance = face_recognition.face_distance(ppl_we_know_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = ppl_we_know_names[best_match_index]

            face_names.append(name)

    To_process_frames = not To_process_frames

    # Display the results
    for (top, right, bottom, left), name in zip(face_location, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
vid_capture.release()
cv2.destroyAllWindows()


