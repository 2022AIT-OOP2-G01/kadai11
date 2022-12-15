import cv2
import time
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

face_cascade_path = '/data_cascade/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

class Image_Processing():
    def __init__(self, image):
        self.image = image
    def face_mosaic(self):
        g_img = self.img2gray()
        faces = face_cascade.detectMultiScale(g_img)
        result = self.image.copy()
        for x, y, w, h in faces:
            result[y: y + h, x: x + w] = [0, 128, 255]
        return result
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
    def binary_img(self):
        #2値化
        gray_img = self.img2gray()
        threshold = 100
        ret, binary_img = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_BINARY)
        return binary_img
        

class CustomLoggingEventHandler(LoggingEventHandler):
    def on_created(self, event):
        root, ext = os.path.splitext(event.src_path)
        if ext == ".png" or ext == ".jpg":
            img = cv2.imread(event.src_path)
            processing = Image_Processing(img)

            file_name = os.path.basename(event.src_path)
            cv2.imwrite('./after/gs/' + file_name, processing.img2gray())
            cv2.imwrite('./after/face/' + file_name, processing.face_detection())
            cv2.imwrite('./after/contour/' + file_name, processing.contour_detection())
            cv2.imwrite('./after/mosaic/' + file_name, processing.face_mosaic())
        

if __name__ == "__main__":
    path = "./original"
    event_handler = CustomLoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
