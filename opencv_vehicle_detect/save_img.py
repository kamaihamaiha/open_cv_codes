import cv2

# opencv 加载显示图片

# 创建窗口
window_name = 'img'
img_path = "D:\\pics\\003.jpg"
img_out_path = "D:\\pics\\003_copy.jpg"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

img = cv2.imread(img_path)

while True:
    cv2.imshow(window_name, img)

    key = cv2.waitKey(0)
    if(key & 0xFF == ord('q')):
        break
    elif(key & 0xFF == ord('s')):
        cv2.imwrite(img_out_path, img)
    else:
        print(key)
        
cv2.destroyAllWindows()
   
