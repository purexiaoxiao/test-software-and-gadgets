def main():
    import moviepy.editor as mpy
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox
    import os

    def begin():
        if text1.get() == '':
            tk.messagebox.showerror('路径为空', '您未选择待处理文件')
            return
        content = mpy.VideoFileClip(path_)
        tk.messagebox.showinfo(title='请等待', message='请耐心等待转码完成')
        content.write_gif('my.gif')
        tk.messagebox.showinfo(title='文件输出路径',
                               message=os.path.abspath('.') + 'my.gif')

    def selectPath():
        nonlocal path_
        path_ = tk.filedialog.askopenfilename(title='选择mp4文件',
                                              filetypes=[('mp4', '.mp4'),
                                                         ('ALL Files', '')])
        text1.delete(0, 'end')
        text1.insert(0, path_)

    def closeThisWindow():
        root.destroy()

    path_ = ''
    root = tk.Tk()
    root.title('肖某的MP4转gif小工具')  #窗口的标题
    root.geometry('500x300+570+200')
    label1 = tk.Label(root, text='请选择文件:')
    text1 = tk.Entry(root, textvariable=path_, bg='white', width=45)
    button1 = tk.Button(root, text='浏览', width=8, command=selectPath)
    button2 = tk.Button(root, text='确定', width=8, command=begin)
    button3 = tk.Button(root, text='退出', width=8, command=closeThisWindow)

    label1.pack()
    text1.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
