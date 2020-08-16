'''labelme批量处理软件
@xx
@version 1.0
'''


def main():
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox
    import os

    def begin():

        if text1.get() == '':
            tk.messagebox.showerror('错误', '您未选择文件')
            return
        for i in path_:
            # print(path_)
            os.system('labelme_json_to_dataset ' + i)
        tk.messagebox.showinfo('处理成功', '您的文件在' + os.path.abspath('.'))

    def selectPath():
        nonlocal path_
        path_ = tk.filedialog.askopenfilenames(title='选择labelme标注后保存的json文件',
                                               filetypes=[('json文件', '.json'),
                                                          ('ALL Files', '')])
        text1.delete(0, 'end')
        text1.insert(0, path_)

    def closeThisWindow():
        root.destroy()

    path_ = ''
    root = tk.Tk()
    root.title('肖某的labelme批量处理json小工具')  #窗口的标题
    root.geometry('500x300+570+200')
    label1 = tk.Label(root, text='请选择labelme标注过后生成的json文件:')
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
