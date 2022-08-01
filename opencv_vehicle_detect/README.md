### 车辆检测

- 创建显示窗口
- 加载显示图片
- 保存文件
- 从摄像头采集视频

#### 保存文件

- `imwrite(name, img)`
    - name: 要保存的文件名
    - img：保存的图片，是 Mat 类型


#### 视频采集

- `VideoCapture()`
- `cap.read()`
- `cap.release()`

查看源码，路径：`D:\codes\open_source_codes\learn_open-cv\opencv\modules\videoio\include\opencv2\videoio.hpp` 其中源码根目录在 `D:\codes\open_source_codes\learn_open-cv\opencv`

##### cap.read()

- 返回 2个值，第一个为状态值，如果可以读到帧则为 true
- 第二个值为视频帧