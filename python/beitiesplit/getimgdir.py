import wx
import os
from pil import image
import numpy as np
#import wx.grid
#import row_col
# row_col
#######################################################################################
app = wx.app()  # wx.app()行创建了一个应用程序对象。每个 wx 程序都需要一个 .app() 对象
frame = wx.frame(none, -1, '请选择待分割的图片文件')  # wx.frame()方法返回一个可以包含小部件的新窗口
frame.setsize(0, 0, 600, 300)  # 函数设置位置和大小(x（左），y（顶部），宽度,高度)
openfiledialog = wx.filedialog(frame, "open", "", "",
                               "all files (*.*)|*.*",
                               wx.fd_open | wx.fd_file_must_exist)

openfiledialog.showmodal()  # 显示窗口
src = openfiledialog.getpath()  # 返回文件的完整路径（如果选择了一个）
np.savez('dir.npz', k_a=src)
openfiledialog.destroy()
