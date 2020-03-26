import face_recognition
import cv2
import numpy as np

import current

#Ladda in ansikten
obama_image = face_recognition.load_image_file("rasmus.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

biden_image = face_recognition.load_image_file("isac.png")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

#Lista med ansikten plus deras namn
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Rasmus",
    "Isac"
]

class FaceReconition:
    def __init__(self, video_source=0):

        #Öppna kameran, om det inte går att öppna, släng ett ValueError
        self.vid = cv2.VideoCapture(0)
        if not self.vid.isOpened():
            raise ValueError("Kan inte nå kameran", video_source)

        #Hämta width och height på kameran
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        #Få en bild från kameran
        if self.vid.isOpened():
            ret, frame = self.vid.read()
        if ret:
            self.get_face(frame)
            return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        else:
            return (ret, None)

    def get_face(self, frame):
        #Konvertera bilden från brg till rbg
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face enqcodings in the frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # gå igenom alla ansikten
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # jämnför bild med kända ansikten
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"

            # Matcha ansikte med de som har laddats in
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            # skriv ut namnet under personens ansikte
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            if current.name != name:
                current.name = name
 
    # Stäng av kameran när programet stängs
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()