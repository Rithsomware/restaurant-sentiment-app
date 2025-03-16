# camera.py
import cv2
import os
import uuid
from config import BASE_DIR, CAMERA_INDEX

def capture_image():
    """
    Captures an image from the webcam and saves it to the captured_images folder.
    Returns the path to the saved image and the captured frame.
    Raises an exception if the camera cannot be opened or the image cannot be captured.
    """
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        raise Exception("Could not open webcam.")
        
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise Exception("Failed to capture image from camera.")
        
    # Create directory to store images
    images_dir = os.path.join(BASE_DIR, 'captured_images')
    os.makedirs(images_dir, exist_ok=True)
    
    # Save the image with a unique filename
    filename = f"{uuid.uuid4()}.jpg"
    file_path = os.path.join(images_dir, filename)
    cv2.imwrite(file_path, frame)
    
    return file_path, frame
