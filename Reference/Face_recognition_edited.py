import face_recognition
import cv2
import numpy as np
import pandas as pd

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)
df=pd.read_excel('UPI.xlsx')
harish_image = face_recognition.load_image_file("E:\\Damn\\Harish.jpg")
harish_face_encoding = face_recognition.face_encodings(harish_image)[0]
landmarks=face_recognition.face_locations(harish_image)

arun_image = face_recognition.load_image_file("E:\\Damn\\Arun.jpg")
arun_face_encoding = face_recognition.face_encodings(arun_image)[0]

aba_image = face_recognition.load_image_file("E:\\Damn\\Aba.jpg")
aba_face_encoding = face_recognition.face_encodings(aba_image)[0]

bhavesh_image = face_recognition.load_image_file("E:\\Damn\\Bhavesh.jpg")
bhavesh_face_encoding = face_recognition.face_encodings(bhavesh_image)[0]

raghav_image = face_recognition.load_image_file("E:\\Damn\\Raghav.jpg")
raghav_face_encoding = face_recognition.face_encodings(raghav_image)[0]

abhay_image = face_recognition.load_image_file("E:\\Damn\\Abhay.jpg")
abhay_face_encoding = face_recognition.face_encodings(abhay_image)[0]

hari_image = face_recognition.load_image_file("E:\\Damn\\Hari.jpg")
hari_face_encoding = face_recognition.face_encodings(hari_image)[0]
# Create arrays of known face encodings and their names
known_face_encodings = [harish_face_encoding,bhavesh_face_encoding,arun_face_encoding,aba_face_encoding,raghav_face_encoding,abhay_face_encoding,hari_face_encoding]
known_face_names = ["Harish","Bhavesh","Arun","Aba","Raghav","Abhay","Hari"]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
flag=1

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    
    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
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
                print(df[df['Name']==name]['UPI'])
                
    
        
            #else:
             #.   print('Face not recognised')
            
    
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
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    
    # Display the resulting image
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

video_capture.release()
cv2.destroyAllWindows()