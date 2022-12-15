import cv2
import time
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

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

class CustomLoggingEventHandler(LoggingEventHandler):
    def on_created(self, event):
        root, ext = os.path.splitext(event.src_path)
        if ext == ".png" or ext == ".jpg":
            img = cv2.imread(event.src_path)
            processing = Image_Processing(img)

            file_name = os.path.basename(event.src_path)
            cv2.imwrite('./after_processing/gray/' + file_name, processing.img2gray())
            cv2.imwrite('./after_processing/face/' + file_name, processing.face_detection())
            cv2.imwrite('./after_processing/contour/' + file_name, processing.contour_detection)
        

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