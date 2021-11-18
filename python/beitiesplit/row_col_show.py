import wx
import numpy as np
import threading
import time
from pil import image, imagedraw


def draw_line(dir, a, b):
    im = image.open(dir)
    draw = imagedraw.draw(im)  # 实例化一个对象
    # a #行 图像的宽:im.size[0]
    # b #列 图像的高:im.size[1]
    a = int(a)
    b = int(b)
    c = im.size[0]
    d = im.size[1]
    for i in range(a):
        draw.line((0, d*(i+1)/a) + (c, d*(i+1)/a),
                  fill=128, width=5)  # 线的起点和终点，线宽
    for j in range(b):
        draw.line((c*(j+1)/b, 0) + (c*(j+1)/b, d), fill=128, width=6)
    return(im.save("00.jpeg"))


class myframe(wx.frame):
    clicknum = 0

    def __init__(
            self):  # __init__(self) 是类的初始化方法，也称构造方法，是一种特殊的魔法方法。__init__(self)在实例化后，会自动调用，而不用手动调用，所以一般把属性设置在_init__()里。
        super().__init__(parent=none, title="图像分割行数与列数", size=(500, 730))  # 初始化窗口信息
        panel = wx.panel(self)  # 框架的父窗口。对于顶级窗口，这个值是none 。#创建面板
        # 模块1 选择签约主体
        self.center()
        data_a = np.load('abc.npz')
        split_row = int(data_a['k_a'])  # 读取行数
        split_col = int(data_a['k_b'])  # 读取列数

        text1 = wx.statictext(parent=panel, id=-1,
                              pos=(10, 7), label="图像分割行数：")
        list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.combobox1 = wx.combobox(parent=panel, id=-1, pos=(100, 5), value=str(split_row),
                                     choices=list1)  # wx.combobox 默认它的文本框是可以修改的

        text2 = wx.statictext(parent=panel, id=-1,
                              pos=(250, 7), label="图像分割列数：")
        list2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.combobox2 = wx.combobox(parent=panel, id=-1, pos=(350, 5), value=str(split_col),
                                     choices=list2)  # wx.combobox 默认它的文本框是可以修改的
        datadir = np.load('dir.npz')
        imgdir = str(datadir['k_a'])
        copybookimg = wx.bitmap(imgdir, wx.bitmap_type_any)
        #img = wx.image(imgdir)
        draw_line(imgdir, str(split_row), str(split_col))
        img3 = wx.image("00.jpeg")
        w1, h1 = copybookimg.getsize()
        if h1 > 400:
            neww1 = (400 * w1) / h1
            newh1 = 400
            img2 = img3.scale(neww1, newh1)
            img2 = wx.bitmap(img2)
            self.image = wx.staticbitmap(panel, -1, img2, pos=(10, 90))
        st1 = wx.statictext(panel, -1, "字帖内容:", pos=(10, 505))
        for i in range(split_col):
            wx.statictext(panel, -1, "第"+str(i+1)+"列:", pos=(10, 530+20*i))

        self.txt1 = wx.textctrl(panel, -1, pos=(60, 530), size=(13.26 *
                                split_row + 23.5, split_col * 20), style=wx.te_multiline)

        # 提交模块
        self.button = wx.button(
            panel, -1, "确定分割", pos=(400, 650), size=(60, 30))  # 在面板上添加控件
        self.bind(wx.evt_button, self.onclick, self.button)  # 将回调函数与按键事件绑定

    def onclick(self, event):  # 回调函数事件
        self.button.setlabel("提交成功")  # 设置
        self.clicknum += 1
        if self.clicknum % 2 == 1:  # 根据按下次数判断
            self.button.setlabel("已经提交")  # 修改按键的标签
            a = self.combobox1.getvalue()
            b = self.combobox2.getvalue()
            c = self.txt1.getvalue()
            np.savez('abc.npz', k_a=a, k_b=b, k_c=c)  # k_c = c碑帖内容保存npz文件
            self.close()


class app(wx.app):
    def oninit(self):
        frame = myframe()
        frame.show()
        return true


app = app()
app.mainloop()
