# 导入需要的包
import random

from yolov5 import Darknet
from camera import LoadStreams, LoadImages
from utils.general import non_max_suppression, scale_coords, check_imshow
from flask import Response
from flask import Flask
from flask import render_template
import time
import torch
import json
import cv2


# initialize a flask object
app = Flask(__name__)
colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(2)]

# initialize the video stream and allow the camera sensor to warmup
with open('yolov5_config.json', 'r', encoding='utf8') as fp:
    opt = json.load(fp)
    print('[INFO] YOLOv5 Config:', opt)

darknet = Darknet(opt)
if darknet.webcam:
    dataset = LoadStreams(darknet.source, img_size=opt["imgsz"], stride=darknet.stride)
else:
    dataset = LoadImages(darknet.source, img_size=opt["imgsz"], stride=darknet.stride)
time.sleep(2.0)


@app.route("/")
def index():
    # return the rendered template
    return render_template("index.html")


def colindex(label):
    if 'no-mask' in label:
        return 0
    else:
        return 1


def detect_gen(dataset, feed_type):
    view_img = check_imshow()
    for path, img, img0s, vid_cap in dataset:
        img = darknet.preprocess(img)

        t1 = time.time()
        pred = darknet.model(img, augment=darknet.opt["augment"])[0]  # 0.22s
        pred = pred.float()
        pred = non_max_suppression(pred, darknet.opt["conf_thres"], darknet.opt["iou_thres"])
        t2 = time.time()

        pred_boxes = []
        for i, det in enumerate(pred):
            if darknet.webcam:  # batch_size >= 1
                feed_type_curr, p, s, im0, frame = "Camera_%s" % str(i), path[i], '%g: ' % i, img0s[
                    i].copy(), dataset.count
            else:
                feed_type_curr, p, s, im0, frame = "Camera", path, '', img0s, getattr(dataset, 'frame', 0)

            s += '%gx%g ' % img.shape[2:]  # print string
            if det is not None and len(det):
                det[:, :4] = scale_coords(
                    img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {darknet.names[int(c)]}{'s' * (n > 1)}, "  # add to string

                for *xyxy, conf, cls_id in det:
                    lbl = darknet.names[int(cls_id)]
                    xyxy = torch.tensor(xyxy).view(1, 4).view(-1).tolist()
                    score = round(conf.tolist(), 3)
                    label = "{}: {}".format(lbl, score)
                    x1, y1, x2, y2 = int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3])
                    pred_boxes.append((x1, y1, x2, y2, lbl, score))
                    if view_img:
                        im0 = darknet.plot_one_box(xyxy, im0, color=colors[colindex(label)], label=label)

            # Print time (inference + NMS)
            # print(pred_boxes)
            print(f'{s}Done. ({t2 - t1:.3f}s)')
            if feed_type_curr == feed_type:
                frame = cv2.imencode('.jpg', im0)[1].tobytes()
                yield b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'


@app.route('/video_feed/<feed_type>')
def video_feed(feed_type):
    """Video streaming route. Put this in the src attribute of an img tag."""
    if feed_type == 'Camera_0':
        return Response(detect_gen(dataset=dataset, feed_type=feed_type),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

    elif feed_type == 'Camera_1':
        return Response(detect_gen(dataset=dataset, feed_type=feed_type),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, threaded=True)
