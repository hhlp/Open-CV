import os
import cv2

class ImageRotate(object):
    def __init__(self, image):
        # Load the image into OpenCV
        self.image_name = image.split("/")[-1]
        self.image = cv2.imread(image, 1)
        # Creates folder for manipulated pictures
        if not os.path.exists("Results/"):
            os.mkdir("Results")

    def rotation(self):
        # Resize the image
        self.image = cv2.resize(self.image, (0, 0), fx=.5, fy=.5)
        # Rotates the image.
        self.image = cv2.rotate(self.image, cv2.cv2.ROTATE_90_CLOCKWISE)
        # Saves new copy of the rotated image.
        cv2.imwrite(f"Results/rotated_{self.image_name}", self.image)
        # Shows the image until a key is pressed.
        cv2.imshow("Rotated Image", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    img = input(r"Enter path to picture  >> ")
    image = ImageRotate(img).rotation()
