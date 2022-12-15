import cv2

class Image_Processing():
    def __init__(self, image):
        self.image = image
    def img2gray(self):
        #画像のグレイスケール化
        gs = self.image.copy()
        gs = cv2.cvtColor(gs, cv2.COLOR_BGR2GRAY)
        return gs
    def face_detection(self):
        #顔検出
        pass
    def contour_detection(self):
        #輪郭抽出
        pass
    def binary_img(self):
        #2値化
        gray_img = self.img2gray()
        threshold = 100
        ret, binary_img = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_BINARY)
        return binary_img
