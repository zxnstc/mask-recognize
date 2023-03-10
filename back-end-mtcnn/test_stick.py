import cv2
from Utils import stick

cap = cv2.VideoCapture(0)

# videoWriter = cv2.VideoWriter('testwrite.avi', cv2.VideoWriter_fourcc(*'MJPG'), 15, (1000,563))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # 从新定义图片大小
        img = cv2.resize(frame, (1000, 563))
        # 添加录像时间
        # img = addtime(img)
        # 实时识别
        img = stick.getface(img)
        # 视频显示
        cv2.imshow('frame', img)
        # 保存视频
        # videoWriter.write(img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("退出视频")
            break
    else:
        break

cap.release()
# videoWriter.release()
cv2.destroyAllWindows()
