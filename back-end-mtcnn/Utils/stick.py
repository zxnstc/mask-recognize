import numpy as np
import cv2
from PIL import Image
import random
import os

''' 人脸识别 '''
def getface(img):
    # 人脸识别数据
    face_cascade = cv2.CascadeClassifier('Utils/haarcascade_frontalface_default.xml')
    # 人眼识别数据
    eye_cascade = cv2.CascadeClassifier('Utils/haarcascade_eye.xml')
    # 二值化,变为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取人脸识别数据
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # 绘画人脸识别数据
        #img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # 根据人脸识别数据添加头像
        img = christmas(img,x,y,w,h)
    return img

image_path = 'paste_image/'

# 从指定目录中随机选取一张图片
def get_one_image(train):
     files = os.listdir(train)
     n = len(files)
     ind = np.random.randint(0, n)
     img_dir = os.path.join(train, files[ind])
     image = Image.open(img_dir)
     return image


def christmas(img,x,y,w,h):
    im = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    #贴纸地址
    #mark = Image.open("image/4.png")
    mark=get_one_image(image_path)
    height = int(w*987/1024)
    mark = mark.resize((w, height))
    layer=Image.new('RGBA', im.size, (0,0,0,0))
    layer.paste(mark, (x,y-height))
    out=Image.composite(layer,im,layer)
    img = cv2.cvtColor(np.asarray(out),cv2.COLOR_RGB2BGR)
    return img
