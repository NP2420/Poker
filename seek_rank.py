import cv2 as cv
import numpy as np 
from ultralytics import YOLO
from display import add_to_frame
# model1 = YOLO('./Training/runs/detect/main/weights/best.pt')
# model1 = YOLO('../Training/runs/classify/main/weights/best.pt')

model1 = YOLO('../Old_Training/Dataset_1/runs/detect/main/weights/best.pt')

def tempname(frame, cards):
    # print("Potential Cards Found: {}".format(len(cards)))

    for i, card in enumerate(cards):

        dst = np.array([
            [0, 0],                             # top-left
            [card.width - 1, 0],                # top-right
            [card.width - 1, card.height - 1],  # bottom-right
            [0, card.height - 1]                # bottom-left
        ], dtype="float32")
        
        matrix = cv.getPerspectiveTransform(card.corners, dst)
        warped = cv.warpPerspective(frame, matrix, (card.width, card.height))
        
        add_to_frame(frame, card, "Card", 0.1) 
        cv.imshow("Card {}".format(i), warped)

        # results1 = model1(warped)
        # pred1 = results1[0]

        # results2 = model2(warped)
        # pred2 = results2[0]

        # results3 = model3(warped)
        # pred3 = results3[0]

        # if len(pred1.boxes) > 0:
        #     label = pred1.names[int(pred1.boxes[0].cls)]
        #     conf = pred1.boxes[0].conf.item()

        #     add_to_frame(frame, card, label, conf)

        # if len(pred2.boxes) > 0:
        #     label = pred2.names[int(pred2.boxes[0].cls)]
        #     conf = pred2.boxes[0].conf.item()

        #     add_to_frame(frame2, card, label, conf)

        # if len(pred3.boxes) > 0:
        #     label = pred3.names[int(pred3.boxes[0].cls)]
        #     conf = pred3.boxes[0].conf.item()

        #     add_to_frame(frame3, card, label, conf)   

        # if pred2.probs is not None:
        #     class_id = pred2.probs.top1
        #     confidence = pred2.probs.data[class_id].item()
        #     class_name = pred2.names[class_id]

        #     add_to_frame(frame2, card, class_name, confidence)
        # else:
        #     print(f"No prediction for card {i}")

        # if pred3.probs is not None:
        #     class_id = pred3.probs.top1
        #     confidence = pred3.probs.data[class_id].item()
        #     class_name = pred3.names[class_id]

        #     add_to_frame(frame3, card, class_name, confidence)
        # else:
        #     print(f"No prediction for card {i}")



        # cv.imshow("Card1 {}".format(i), new_frame)

        return warped


