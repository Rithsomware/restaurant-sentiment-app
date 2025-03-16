# sentiment.py
import cv2

def analyze_sentiment(image):
    """
    Analyzes the image for facial expression sentiment using Haar cascades.
    Returns a sentiment label as a string:
      - "Happy" if a smile is detected,
      - "Neutral" if a face is detected without a smile,
      - "No face detected" if no face is found.
    """
    # Convert to grayscale for cascade detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load Haar cascades for face and smile detection (using OpenCV's built-in data)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) == 0:
        return "No face detected"
    
    # For each face detected, check for a smile in the region of interest
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
        if len(smiles) > 0:
            return "Happy"
    
    return "Neutral"
