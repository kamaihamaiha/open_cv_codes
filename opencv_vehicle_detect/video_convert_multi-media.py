import cv2


four_cc = cv2.VideoWriter(*'MJPG')
# 最后一个是摄像头分辨率，根据实际摄像头分辨率来写
vw = cv2.VideoWriter("out.mp4", four_cc, 25, (1280, 720))

# create window
cv2.namedWindow('cap_video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 360)

# get video device(我的电脑没有摄像头，没法测试) 需要购买摄像头
cap = cv2.VideoCapture(0)

# 不停的读取摄像头(如果摄像头打开的话)
while cap.isOpened():
    # 从摄像头读视频帧
    ret, frame = cap.read()

    if ret == True:
        # 将视频帧显示到窗口中
        cv2.imshow('video', frame)
        # 避免窗口因为采集的视频分辨率大，把窗口撑大
        cv2.resizeWindow('video', 640, 360)

        # 写数据到多媒体文件
        vw.write(frame)

        key = cv2.waitKey(3)
        if(key & 0xff == ord('q')):
            break
    else:
        break
    
# release VideoCapture
cap.release()

# 释放 VideoWriter
vw.release()

cv2.destroyAllWindows()
