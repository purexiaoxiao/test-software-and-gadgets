def main():
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox
    import os
    import zipfile

    def myZipToFile():
        if text1.get() == '':
            tk.messagebox.showerror('路径为空', '您未选择待压缩文件')
            return
        tk.messagebox.showinfo('请等待', '请耐心等待解压缩完成')
        f = zipfile.ZipFile(path_, 'r')
        # print(f.namelist())
        for file in f.namelist():
            f.extract(file, 'temp/')
        tk.messagebox.showinfo('压缩完成',
                               '您的文件在' + os.path.abspath('.') + '\\temp')

    def selectPath():
        nonlocal path_
        path_ = tk.filedialog.askopenfilename(title='选择压缩文件',
                                              filetype=[('压缩文件', '.zip')])
        text1.delete(0, 'end')
        text1.insert(0, path_)

    def closeThisWindow():
        root.destroy()

    path_ = ''
    root = tk.Tk()
    root.title('肖某的c++压缩小工具')
    root.geometry('500x300+570+200')
    label1 = tk.Label(root, text='请选择待解压的文件:')
    text1 = tk.Entry(root, textvariable=path_, bg='white', width=45)
    button1 = tk.Button(root, text='浏览', width=8, command=selectPath)
    button2 = tk.Button(root, text='确定', width=8, command=myZipToFile)
    button3 = tk.Button(root, text='退出', width=8, command=closeThisWindow)
    label1.pack()
    text1.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
