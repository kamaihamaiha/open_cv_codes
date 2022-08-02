### 车辆检测

[课程视频地址](https://www.bilibili.com/video/BV1E34y1W7U5?p=9&vd_source=82b7ac2fbd7ece380f983e2c23199d99)

查看源码，路径：`D:\codes\open_source_codes\learn_open-cv\opencv\modules\videoio\include\opencv2\videoio.hpp` 其中源码根目录在 `D:\codes\open_source_codes\learn_open-cv\opencv`

- 创建显示窗口
- 加载显示图片
- 保存文件
- 从摄像头采集视频
- 从多媒体文件中读取视频帧
- [将视频数据录制成多媒体文件](./docs/section_6.md)

#### 保存文件

- `imwrite(name, img)`
    - name: 要保存的文件名
    - img：保存的图片，是 Mat 类型


#### 视频采集

[代码](./cap_video.py)

- `VideoCapture()`
- `cap.read()`
- `cap.release()`


##### cap.read()


- 返回 2个值，第一个为状态值，如果可以读到帧则为 true
- 第二个值为视频帧

#### 从多媒体文件中读取视频帧

[代码](./read_video_file.py)