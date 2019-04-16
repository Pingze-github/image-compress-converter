# Image-compress-converter

图片压缩转换器。

用于分发图片包时，在不损失图片质量情况下，尽量压缩图片体积。

## 使用

## 说明

### 元数据

图片携带的元数据会被清除。

### 压缩损失

对于jpeg和webp的有损压缩，质量默认为控制为95（完美）。

可以通过参数控制到更低质量。推荐75，体积可以减小到一半左右，而肉眼难以分辨差别。

### 格式

#### Advanced mode

最先进模式，可以保证被chromium内核浏览器解析。

选择目标格式为WebP。理由：
+ 在同等质量下，输出文件体积比JPEG更小。
+ 支持RGBA通道。
+ 支持Animated WebP。

图像文件一律转为RGBA通道的webp，后缀名.webp。

#### Compatible mode

兼容模式。适用于各种场景。

RGB通道文件一律转为JPG格式，后缀名.jpg。
RGBA通道文件转为PNG格式，但使用.jpg后缀名。
GIF格式文件直接复制。

#### [Default] Advanced & Compatible mode

兼顾先进性和兼容性的模式。可以被大多数图片浏览软件解析。

静态图像文件一律转为webp格式。
动态图像文件（GIF）直接复制。
