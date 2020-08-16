import tkinter as tk
import tkinter.messagebox
from itertools import count

from PIL import Image, ImageTk

import package


class ImageLabel(tk.Label):
    ''' from http://cn.voidcc.com/question/p-nanjlyhm-uz.html'''
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 1000
        try:
            if len(self.frames) == 1:
                self.config(image=self.frames[0])

            else:
                self.next_frame()
        except:
            pass

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


def package_():
    tk.messagebox.showinfo('请耐心等待', '请耐心等待安装完成')
    package.main()
    tk.messagebox.showinfo('完成', '相关库以安装文成')


def start():
    def datafactor():
        datafactory.main()

    def mysort1():
        sort1.main()

    def mysort2():
        sort2.main()

    def mysort3():
        sort3.main()

    def multiplyFiles():
        mulFileToOne.main()

    def quit():
        window.destroy()

    import datafactory
    import sort1
    import sort2
    import sort3
    import mulFileToOne
    import about
    import smallToolsByXx
    '''以下为构建窗体'''
    lbl.pack()
    bt1 = tk.Button(window, text='生成文件', command=datafactor)
    bt2 = tk.Button(window, text='排序1', command=mysort1)
    bt3 = tk.Button(window, text='排序2', command=mysort2)
    bt4 = tk.Button(window, text='排序3', command=mysort3)
    bt5 = tk.Button(window, text='多文件信息合成', command=multiplyFiles)
    bt6 = tk.Button(window, text='其他', command=smallToolsByXx.main)
    bt7 = tk.Button(window, text='关于', command=about.main)
    bt8 = tk.Button(window, text='退出', command=quit)
    bt1.pack()
    bt2.pack()
    bt3.pack()
    bt4.pack()
    bt5.pack()
    bt6.pack()
    bt7.pack()
    bt8.pack()
    window.update()
    window.deiconify()


window = tk.Tk()
window.title('主页面')
lbl = ImageLabel(window)
lbl.pack()
lbl.load('my.gif')
lbl.pack_forget()
tk.messagebox.showinfo('初次使用', '初次使用请先安装库之后再运行')
window.withdraw()
root = tk.Tk()
root.geometry('100x200')
root.title('启动页')
tk.Button(root, text='安装库', command=package_).pack()
tk.Button(root, text='启动工具', command=start).pack()
root.mainloop()