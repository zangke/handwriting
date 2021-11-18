# -*- coding: utf-8 -*-
 
import wx
import os
from pil import image
import numpy as np
#import wx.grid
#import row_col
#row_col
#######################################################################################
data_a = np.load('dir.npz')
src=str(data_a['k_a'])#地址
 
 
def splitimage(src, rownum, colnum, dstpath): #分割图像，（输入图片路径，分割行数，分割列数，输出图片路径）
 
  img = image.open(src)
  src=src.replace('jpg','jpeg')
 
  print(src)
  #os.getcwd()
  w, h = img.size
  if rownum <= h and colnum <= w:
    print('原碑帖图片信息: %sx%s, %s, %s' % (w, h, img.format, img.mode))
    print('')