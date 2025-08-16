import cv2
from ultralytics import YOLO

import cv2 as cv
from card_finder import find_cards, catalogue
from seek_rank import tempname

def hi():
    cards = [] #List of cards in current frame

    isTrue, frame = cap.read()

    possible_cards = find_cards(frame)
    cards = []
    catalogue(possible_cards, cards)

    tempname(frame, cards)

    cv.imshow('Frame', frame)
    
# Load your trained model
model = YOLO('..\\Training\\Classification_3\\runs\\classify\\train3\\weights\\last.pt')
# Open webcam (0 is usually default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # hi()

    # Run inference on the current frame
    results = model(frame)

    # results[0].plot() returns an image with detections drawn on it
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow('YOLOv8 Webcam Detection', annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


