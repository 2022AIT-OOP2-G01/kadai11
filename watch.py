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
        edges = cv2.Canny(self.image, 100, 400)
        return edges
