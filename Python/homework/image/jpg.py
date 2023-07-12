from PIL import Image, ImageFilter

# 打开图片
image = Image.open("image/test.jpg")

# 展示原始图片
image.show()

# 模式“L”为灰色图像
# 模式“1”为二值图像，非黑即白
# 模式“P”为8位彩色图像
gray_image = image.convert("L")
gray_image.show()

# 缩放图片
resized_image = gray_image.resize((250, 300))
resized_image.show()

# 模糊化处理
blurred_image = resized_image.filter(ImageFilter.BLUR)
blurred_image.show()

# 保存结果
blurred_image.save("homework/image/test1.jpg")
