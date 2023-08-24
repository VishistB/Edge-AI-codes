import cv2
import numpy as np

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the laptop camera (change the index if you have multiple cameras)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = frame[y-20:y+h+20, x-20:x+w+20]
        blurred_face = cv2.medianBlur(face_roi, ksize=15) 
        frame[y-20:y+h+20, x-20:x+w+20] = blurred_face

    #canny for sharpening;
    blurred = cv2.GaussianBlur(frame, (5, 5), 10)  
    unsharp_mask = cv2.addWeighted(frame, 1.5, blurred, -0.5, 0) 

    cv2.imshow('Video Feed', unsharp_mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
