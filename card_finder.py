import cv2 as cv
import numpy as np
from card import Card


# Detect card shaped objects (4 sides)

MIN_AREA = 1000
        
def find_cards(frame):
    # Processes a frame and finds all contours that could be cards

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #Gray Scale

    blur = cv.GaussianBlur(gray, (5, 5), 0) #Gaussian Blur (Reduce Noise)

    canny = cv.Canny(blur, 50, 150) #Canny (Edge Detection)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5)) 
    dilate = cv.dilate(canny, kernel, iterations=1) #Dilation to connect gaps in edges (Optional)

    contours, _ = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) #Find Contours

    # Finding card shaped contours
    possible_cards = []

    for contour in contours:

        #Remove small noise
        area = cv.contourArea(contour)
        if area < MIN_AREA:
            continue

        # Approximate the contour
        peri = cv.arcLength(contour, True) #Calculate perimeter of closed contour
        approx = cv.approxPolyDP(contour, 0.03 * peri, True) #Simplifies the contour shape

        if len(approx) == 4 and cv.isContourConvex(approx): #4 vertices = quadrilateral
            possible_cards.append(approx)

    return possible_cards

def catalogue(possible_cards, cards):
    # Takes in a list of contours and creates card objects from them

    # cards = [Card(contour) for contour in possible_cards]

    for card_contour in possible_cards:
        new_card = Card(card_contour)

        cards.append(new_card)


