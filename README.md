# Image-compress-converter

图片压缩转换器。

用于分发图片包时，在不损失图片质量情况下，尽量压缩图片体积。

## 使用

## 压缩损失

对于有损压缩，质量默认为控制为75。
此时肉眼观察几乎没有差别，体积可以（相较完美）减小到一半左右。

如果希望完美转换，可使用参数控制质量参数到95。

## 格式

### Advanced mode

最先进模式，可以保证被chromium内核浏览器解析。

选择目标格式为WebP。理由：
+ 在同等质量下，输出文件体积比JPEG更小。
+ 支持RGBA通道。
+ 支持Animated WebP。

图像文件一律转为RGBA通道的webp，后缀名.webp。

### Compatible mode

兼容模式。适用于各种场景。

RGB通道文件一律转为JPG格式，后缀名.jpg。
RGBA通道文件转为PNG格式，但使用.jpg后缀名。
GIF格式文件直接复制。

### [Default] Advanced & Compatible mode

兼顾先进性和兼容性的模式。可以被大多数图片浏览软件解析。

静态图像文件一律转为webp格式。
动态图像文件（GIF）直接复制。
