def main():
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox
    import os
    import xlwt
    import zipfile

    def mytozip():
        if text2.get() == '':
            tk.messagebox.showerror('名称错误', '压缩文件名称为空')
            return
        if text1.get() == '':
            tk.messagebox.showerror('路径为空', '您未选择待压缩文件')
            return
        tk.messagebox.showinfo('请等待', '请耐心等待压缩完成')
        f = zipfile.ZipFile(text2.get() + '.zip', 'w', zipfile.ZIP_DEFLATED)
        for i in path_:
            f.write(i)
        f.close()
        tk.messagebox.showinfo(
            '压缩完成', '文件路径为:' + os.path.abspath('.') + '\\' + text2.get())

    def selectPath():
        nonlocal path_
        path_ = tk.filedialog.askopenfilenames(title='选择文件')
        text1.delete(0, 'end')
        text1.insert(0, path_)

    def closeThisWindow():
        root.destroy()

    path_ = ''
    root = tk.Tk()
    root.title('肖某的文件压缩小工具')  #窗口的标题
    root.geometry('500x300+570+200')
    label1 = tk.Label(root, text='请选择文件:')
    text1 = tk.Entry(root, textvariable=path_, bg='white', width=45)
    button1 = tk.Button(root, text='浏览', width=8, command=selectPath)
    button2 = tk.Button(root, text='确定', width=8, command=mytozip)
    button3 = tk.Button(root, text='退出', width=8, command=closeThisWindow)
    label = tk.Label(root, text='请输入压缩后的文件名(不需要后缀)')
    text2 = tk.Entry(root, bg='white', width=10)
    label1.pack()
    text1.pack()
    button1.pack()
    label.pack()
    text2.pack()
    button2.pack()
    button3.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
