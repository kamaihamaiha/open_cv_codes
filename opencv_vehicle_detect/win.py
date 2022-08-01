import cv2

# 1.创建窗口
cv2.namedWindow('new', cv2.WINDOW_NORMAL)
cv2.resizeWindow('new', 640, 480)

# 2. 显示窗口
cv2.imshow('new', 0)

# 接收键盘和鼠标事件。为了是让窗口显示，不至于一闪而过. 参数是 ms，如果想一直显示则传 0
key = cv2.waitKey(0)

# 输入 q 退出
if(key == 'q'):
    exit()

# 3. 销毁
cv2.destroyAllWindows()