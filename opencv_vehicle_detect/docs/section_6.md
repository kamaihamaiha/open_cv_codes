### 将视频数据录制成多媒体文件

使用例子说明文档：D:\codes\open_source_codes\learn_open-cv\opencv\doc\py_tutorials\py_gui\py_video_display\py_video_display.markdown

[代码](./../video_convert_multi-media.py)

- `VideoWriter`
- `write()`  
  - 其中的步骤，包括把视频帧数据先编码，然后再写入文件
  - 参数：分辨率、帧率
- `release()`

#### VideoWriter

- param1: 输出文件
- param2: 多媒体文件格式(VideoWriter_fourcc) 
- param3: fps
- param4: 分辨率
