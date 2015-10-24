# -*- coding: UTF-8 -*-

from Tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap',"django","jj","ii","kk","ff","gg","rr","tt"]

scrollbar = Scrollbar(root)				
scrollbar.pack( side = LEFT)

listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root, yscrollcommand = scrollbar.set)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
scrollbar.set(100,200)
scrollbar.config( command = listb2.yview )
root.mainloop()                 # 进入消息循环