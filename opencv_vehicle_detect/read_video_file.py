import cv2
from cv2 import waitKey

# create window
cv2.namedWindow('cap_video', cv2.WINDOW_NORMAL)

# get frame from video file
cap = cv2.VideoCapture("D:\\videos\\intro.mp4")

# 不停的读取
while True:
    # 读视频帧
    ret, frame = cap.read()

    # 将视频帧显示到窗口中
    cv2.imshow('video', frame)

    # 40ms 25fps
    key = cv2.waitKey(40)
    if(key & 0xff == ord('q')):
        break

# release VideoCapture
cap.release()
cv2.destroyAllWindows()
