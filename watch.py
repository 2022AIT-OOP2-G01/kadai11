import cv2
# https://github.com/opencv/opencv/blob/master/data/haarcascades/
class ImageProcessing():
    def __init__(self, image):
        self.image = image

    def img2gray(self):
        #画像のグレイスケール化
        pass

    def face_detection(self):
        
        face_image = self.image.copy()
        cascade_path= "./data_cascade/haarcascade_frontalface_default.xml"
        #self.imageをreturnで返す
        # self = cv2.imread('human.jpeg')
        gray_scale = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        #カスケード分類機の特徴量を取得
        cascade = cv2.CascadeClassifier(cascade_path)
        
        facerect = cascade.detectMultiScale(gray_scale, minSize=(50,50))
        color=(0 ,0, 255)
        # 検出した場合
        if len(facerect) > 0:

            #検出した顔を囲む矩形の作成
            for rect in facerect:
                cv2.rectangle(face_image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

        cv2.imwrite('./img/test.jpeg', face_image)
        return face_image
        

if __name__ == "__main__":
    app = ImageProcessing(cv2.imread('./img/human.jpeg'))
    app.face_detection()

    

