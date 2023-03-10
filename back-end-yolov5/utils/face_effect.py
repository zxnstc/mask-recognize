import os
import cv2
import numpy as np
from PIL import Image

image_path = './image'


# 从指定目录中随机选取一张图片


def get_one_image(train):
    files = os.listdir(train)
    n = len(files)
    ind = np.random.randint(0, n)
    img_dir = os.path.join(train, files[ind])
    image = Image.open(img_dir)
    return image


def make_effect(img, x, y, w, h):
    im = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    mark = get_one_image(image_path)
    mark = mark.resize((w, h))
    layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
    layer.paste(mark, (x, y))
    out = Image.composite(layer, im, layer)
    img = cv2.cvtColor(np.asarray(out), cv2.COLOR_RGB2BGR)
    return img
