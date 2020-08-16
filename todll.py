def main():
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox
    import os

    def begin():

        if text2.get() == '':
            tk.messagebox.showerror('错误', '您未指定文件名')
            return
        os.system('g++ -shared ' + path_ + ' -o ' + text2.get() + '.dll' +
                  ' -std=c++17')
        tk.messagebox.showinfo('编译完成', text2.get() + '.dll生成完成')
        tk.messagebox.showinfo(
            '文件路径',
            '您的文件输出目录为: ' + os.path.abspath('.') + text2.get() + '.dll')

    def selectPath():
        nonlocal path_
        path_ = tk.filedialog.askopenfilename(title='选择mp4文件',
                                              filetypes=[('c++源文件', '.cpp'),
                                                         ('ALL Files', '')])
        text1.insert(0, path_)

    def closeThisWindow():
        root.destroy()

    path_ = ''
    root = tk.Tk()
    root.title('肖某的c++编译dll文件小工具')  #窗口的标题
    root.geometry('500x300+570+200')
    label1 = tk.Label(root, text='请选择文件:')
    text1 = tk.Entry(root, textvariable=path_, bg='white', width=45)
    button1 = tk.Button(root, text='浏览', width=8, command=selectPath)
    button2 = tk.Button(root, text='确定', width=8, command=begin)
    button3 = tk.Button(root, text='退出', width=8, command=closeThisWindow)
    label = tk.Label(root, text='请输入dll的文件名(不需要后缀)')
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
