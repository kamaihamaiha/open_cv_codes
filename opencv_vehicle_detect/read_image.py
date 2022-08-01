import cv2

# opencv 加载显示图片

# 创建窗口
window_name = 'img'
img_path = "D:\\pics\\003.jpg"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

img = cv2.imread(img_path)

cv2.imshow(window_name, img)

key = cv2.waitKey(0)
if(key == 'q'):
    cv2.destroyAllWindows()
   
