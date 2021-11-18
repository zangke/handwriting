import os
os.system("python ./getimgdir.py")
os.system("python ./row_col.py")
os.system("python ./row_col_show.py")
os.system("python ./split_copybook.py")
os.unlink('00.jpeg')
os.unlink('abc.npz')
os.unlink('dir.npz')