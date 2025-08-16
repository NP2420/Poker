import cv2 as cv
import numpy as np

class Card:
    def __init__(self, contour):
        self.contour = contour
        self.corners = self.order_contour(contour.reshape(4, 2))
        self.width, self.height = self.get_dimensions()
        # self.center = self.calc_center()
        self.rank = "Unknown"
        self.suit = "Unknown"

    # def calc_center(self):
    #     x, y, w, h = cv.boundingRect(self.contour)
    #     return (x + w // 2, y + h // 2)

    def get_dimensions(self):
        (tl, tr, br, bl) = self.corners
        widthA = np.linalg.norm(br - bl)
        widthB = np.linalg.norm(tr - tl)
        maxWidth = max(int(widthA), int(widthB))

        heightA = np.linalg.norm(tr - br)
        heightB = np.linalg.norm(tl - bl)
        maxHeight = max(int(heightA), int(heightB))

        return (maxWidth, maxHeight)
    
    def order_contour(self, pts):
        rect = np.zeros((4, 2), dtype="float32")

        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]  # top-left
        rect[2] = pts[np.argmax(s)]  # bottom-right

        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]  # top-right
        rect[3] = pts[np.argmax(diff)]  # bottom-left

        return rect
    
    def __str__(self):
        return f"Card(Rank: {self.rank}, Suit: {self.suit}, Center: {self.center}, Width: {self.width}, Height: {self.height})"