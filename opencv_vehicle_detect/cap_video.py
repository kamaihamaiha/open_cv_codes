import cv2
from cv2 import waitKey

# create window
cv2.namedWindow('cap_video', cv2.WINDOW_NORMAL)

# get video device(我的电脑没有摄像头，没法测试) 需要购买摄像头
cap = cv2.VideoCapture(0)

# 不停的读取摄像头
while True:
    # 从摄像头读视频帧
    ret, frame = cap.read()

    # 将视频帧显示到窗口中
    cv2.imshow('video', frame)

    key = cv2.waitKey(3)
    if(key & 0xff == ord('q')):
        break

# release VideoCapture
cap.release()
cv2.destroyAllWindows()
