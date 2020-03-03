# imported facial recognition library
# Used for recognizing faces
import face_recognition
# OpenCV library
import cv2 as cv
# To handle those mathmatical equation
import numpy as np

# Get a reference to webcam #0 (the default one)
def Facial_Recog():
    video_capture = cv.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    justyn_image = face_recognition.load_image_file("Pictures\justyn.jpg")
    justyn_face_encoding = face_recognition.face_encodings(justyn_image)[0]

    # Load a second sample picture and learn how to recognize it.
    dad_image = face_recognition.load_image_file("Pictures\dad.jpg")
    dad_face_encoding = face_recognition.face_encodings(dad_image)[0]

    mama_image = face_recognition.load_image_file("Pictures\mama.jpg")
    mama_face_encoding = face_recognition.face_encodings(mama_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        justyn_face_encoding,
        dad_face_encoding,
        mama_face_encoding

    ]
    # This creates the name around the user so when the justyn steps in to view it has his name.
    known_face_names = [
        "Justyn",
        "DAD",
        "mama"
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    # now lets get the main loop working so the camera will:
    # 1)Continue
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"



                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv.FILLED)
            font = cv.FONT_HERSHEY_DUPLEX
            cv.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv.waitKey(1) & 0xFF == ord('q'):
             break
        if cv.waitKey(1) == ord('p') & 0xFF:
            name = input("Please enter your name: ")
            cv.imwrite(name + ".jpg", frame)
            break

    # Release handle to the webcam
    video_capture.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    Facial_Recog()
