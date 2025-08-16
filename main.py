import cv2 as cv
from card_finder import find_cards, catalogue
from seek_rank import tempname
import os

# names = []





def main():
        # List of class names
    class_names = ['AS', 'AC', 'AD', 'AH',
                    '2S', '2C', '2D', '2H',
                    '3S', '3C', '3D', '3H',
                    '4S', '4C', '4D', '4H',
                    '5S', '5C', '5D', '5H',
                    '6S', '6C', '6D', '6H',
                    '7S', '7C', '7D', '7H',
                    '8S', '8C', '8D', '8H',
                    '9S', '9C', '9D', '9H',
                    '10S', '10C', '10D', '10H',
                    'JS', 'JC', 'JD', 'JH',
                    'QS', 'QC', 'QD', 'QH',
                    'KS', 'KC', 'KD', 'KH']

    class_index = 0
    save_counter = 0


    capture = cv.VideoCapture(0)

    cards = [] #List of cards in current frame

    while True:
        isTrue, frame = capture.read()

        possible_cards = find_cards(frame)
        cards = []
        catalogue(possible_cards, cards)

        # frame2 = frame.copy()
        # frame3 = frame.copy()
        save = tempname(frame, cards)

        cv.imshow('Detection', frame)
        # cv.imshow('Classy_OG', frame2)
        # cv.imshow('Classy_New', frame3)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break
        # elif cv.waitKey(20) & 0xFF==ord('s'):
        #     tempname(frame3, cards)

        # Replace this in your loop
        if cv.waitKey(20) & 0xFF == ord('u'):
            current_class = class_names[class_index]
            class_dir = os.path.join('./Training/My_Images/Set1', current_class)
            os.makedirs(class_dir, exist_ok=True)

            # Count existing files to avoid overwriting
            num_files = len([f for f in os.listdir(class_dir) if os.path.isfile(os.path.join(class_dir, f))])

            # Save image
            cv.imwrite(os.path.join(class_dir, f'{current_class}_{num_files + 1}.jpg'), save)
            save_counter += 1

            print(f"Saved {save_counter}/10 for class {current_class}")

            # If 1 images saved for this class, go to the next one
            if save_counter >= 10:
                save_counter = 0
                class_index += 1

                if class_index >= len(class_names):
                    print("✅ All classes done!")
                    class_index = len(class_names) - 1  # Freeze at last class, or exit loop if you want


    capture.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()