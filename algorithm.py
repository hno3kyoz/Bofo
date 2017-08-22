from PIL import Image
from pylab import *
import pylab


# from __future__ import print_function
im = array(Image.open('test.jpg'))
#读取为灰度图像
im = array(Image.open('test.jpg').convert('L'))



"""小练习 读取图像的轮廓图"""
# 新建一个图像
figure()
# 不使用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im,origin='image')
axis('equal')
axis('off')
# show()

figure()
hist(im.flatten(),128)
show()

# ###小练习，在图像上标注点和线段###
# imshow(im)
# #假设一些点
# x = [100,100,400,400]
# y = [200,500,200,500]
# #画各种线
# plot(x,y,'r*')
# plot(x,y)#默认为蓝色实线
# plot(x,y,'r*')#红色星装标记
# plot(x,y,'go-')#带有圆标记的绿线
# plot(x,y,'ks:')#带有正方形标记的黑色点线
# """颜色选项：'b'蓝色，g绿色，r红色，c青色，m品红，y黄色，k黑色，w白色
# 线型：'-'实线，'--'虚线，':'点线
# 标记：'.'点，o圆圈，s正方形，*星形，+加号，x叉号"""
# plot(x[:2],y[:2])
# title('Plotting:"empire.jpg"')
# axis('off')
# show()

# print(im.format,im.size,im.mode)

# out = im.transpose(Image.FLIP_LEFT_RIGHT)
# out = im.convert("L")

# out = im.thumbnail((128,128))
# out2 = im.resize((500,128))

