import wx
import numpy as np
import sys
import time
import os


class myframe(wx.frame):
    clicknum = 0

    def __init__(self):  # __init__(self) 是类的初始化方法，也称构造方法，是一种特殊的魔法方法。__init__(self)在实例化后，会自动调用，而不用手动调用，所以一般把属性设置在_init__()里。
        super().__init__(parent=none, title="图像分割行数与列数", size=(500, 730))  # 初始化窗口信息
        panel = wx.panel(self)  # 框架的父窗口。对于顶级窗口，这个值是none 。#创建面板
        # 模块1 选择签约主体
        self.center()
        text1 = wx.statictext(parent=panel, id=-1,
                              pos=(10, 7), label="图像分割行数：")
        list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        # wx.combobox 默认它的文本框是可以修改的
        self.combobox1 = wx.combobox(
            parent=panel, id=-1, pos=(100, 5), value="5", choices=list1)

        text2 = wx.statictext(parent=panel, id=-1,
                              pos=(250, 7), label="图像分割列数：")
        list2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        # wx.combobox 默认它的文本框是可以修改的
        self.combobox2 = wx.combobox(
            parent=panel, id=-1, pos=(350, 5), value="4", choices=list2)

        datadir = np.load('dir.npz')
        imgdir = str(datadir['k_a'])
        copybookimg = wx.bitmap(imgdir, wx.bitmap_type_any)
        img = wx.image(imgdir)
        w1, h1 = copybookimg.getsize()
        if h1 > 400:
            neww1 = (400*w1)/h1
            newh1 = 400
            img2 = img.scale(int(neww1), newh1)
            img2 = wx.bitmap(img2)
            self.image = wx.staticbitmap(panel, -1, img2, pos=(10, 90))

        st1 = wx.statictext(panel, -1, "字帖内容:", pos=(10, 505))

        self.txt1 = wx.textctrl(
            panel, -1, pos=(60, 530), size=(int(13.26*1+23.5), 140), style=wx.te_multiline)

        # 提交模块
        self.button = wx.button(
            panel, -1, "确定行列", pos=(200, 40), size=(60, 30))  # 在面板上添加控件
        self.bind(wx.evt_button, self.onclick, self.button)  # 将回调函数与按键事件绑定

    def onclick(self, event):  # 回调函数事件
        self.button.setlabel("提交成功")  # 设置
        self.clicknum += 1
        if self.clicknum % 2 == 1:  # 根据按下次数判断
            self.button.setlabel("已经提交")  # 修改按键的标签
            a = self.combobox1.getvalue()
            b = self.combobox2.getvalue()
            np.savez('abc.npz', k_a=a, k_b=b)
            # time.sleep(0.1)
            self.close()


class app(wx.app):
    def oninit(self):
        frame = myframe()
        frame.show()
        return true


app = app()
app.mainloop()
# time.sleep(2)
# sys.exit(0)
