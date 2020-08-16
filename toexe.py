def main():
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox
    import os

    def begin():
        if path_ == '':
            tk.messagebox.showerror('错误', '路径为空')
            return
        tk.messagebox.showinfo('请耐心等待', '请耐心等待打包完成')
        os.system('pyinstaller -F -w ' + path_)
        tk.messagebox.showinfo('完成', '打包完成')
        tk.messagebox.showinfo('注意', '如果提示爆栈请使用spec打包方式')

    def selectPath():
        nonlocal path_
        path_ = tk.filedialog.askopenfilename(title='选择python文件',
                                              filetypes=[('python源代码', '.py'),
                                                         ('ALL Files', '')])
        text1.delete(0, 'end')
        text1.insert(0, path_)

    def closeThisWindow():
        root.destroy()

    path_ = ''
    root = tk.Tk()
    root.title('肖某一件打包python文件小工具')  #窗口的标题
    root.geometry('500x300+570+200')
    label1 = tk.Label(root, text='请选择python文件:')
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
