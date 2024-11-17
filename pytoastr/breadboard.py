import cv2
import numpy
import os

# check size (bounding box) is square
def isSquare(siz):
    ratio = abs(siz[0] - siz[1]) / siz[0]
    #print (siz, ratio)
    if ratio < 0.1:
        return True
    else:
        return False

def create_folder_from_file(file_path):
    # Extract the file name without extension
    folder_name = os.path.splitext(os.path.basename(file_path))[0]

    # Create a new directory
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")

    return folder_name

class Breadboard:
    def __init__(self, image):
        self.image, self.binary_image = self.load_breadboard_image(image)
        self.grid = self.get_grid()

    # image: Path to image
    def load_breadboard_image(self, image):
        #folder_name = create_folder_from_file(image)
        output_image = cv2.imread(image)

        gray_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

        #cv2.imshow('bread_board', output_image)
        #cv2.imshow('binary_bread_board', binary_image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        return output_image, binary_image

    def get_grid(self):
        img = self.image
        dst = self.binary_image
        # clean up
        for i in range(5):
            dst = cv2.erode(dst, None)
        for i in range(3):
            dst = cv2.dilate(dst, None)

        cv2.imshow("dilated", dst)
        # find contours with hierarchy
        cont, hier = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # each contour
        for i in range(len(cont)):
            c = cont[i]
            h = hier[0, i]
            # print(h)
            #if isSquare(cv2.minAreaRect(c)[1]):
            if cv2.contourArea(c) < 300:
                #print(cv2.contourArea(c))
                img = cv2.drawContours(img, cont, i, (255, 0, 0), -1)

        cv2.imshow("contours", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return [0]


breadboard = Breadboard("/Users/andrewburns/Desktop/Fall 24/CVE/toastr.ai/testing/images/empty_breadboard.jpg")

