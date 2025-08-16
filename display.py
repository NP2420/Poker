import cv2 as cv
# from card import Card

def add_to_frame(frame, card, label, conf):
    # Draws card contours and info on the original frame

    cv.drawContours(frame, [card.contour], -1, (0, 255, 0), 3) #Draw shape on original frame
    cv.putText(frame, f"{label} ({conf:.2f})",
                (int(card.corners[0][0]), int(card.corners[0][1] - 10)),
                cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    

