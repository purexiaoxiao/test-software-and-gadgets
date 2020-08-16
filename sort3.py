def main():
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox
    import os
    import xlwt

    def mysort():
        if path_ == '':
            tk.messagebox.showerror('错误', '您未选择文件')
            return

        txt = open(path_, 'r')
        label = txt.readline()
        data = [i.split('\t') for i in txt.readlines()]
        txt.close()

        data.sort(key=lambda x: int(x[-1]), reverse=True)
        txt = open(path_, 'w')
        txt.write(label)
        for i in data:
            txt.write('\t'.join(i))
        tk.messagebox.showinfo('完成', '源文件已排序完毕')
        return

    def selectPath():
        nonlocal path_
        path_ = tk.filedialog.askopenfilename(title='选择xls文件',
                                              filetypes=[('xls文件', '.xls'),
                                                         ('ALL Files', '')])
        text1.delete(0, 'end')
        text1.insert(0, path_)

    def closeThisWindow():
        root.destroy()

    path_ = ''
    root = tk.Tk()
    root.title('肖某的排序3')  #窗口的标题
    root.geometry('500x300+570+200')
    label1 = tk.Label(root, text='请选择待排序的文件:')
    text1 = tk.Entry(root, textvariable=path_, bg='white', width=45)
    button1 = tk.Button(root, text='浏览', width=8, command=selectPath)
    button2 = tk.Button(root, text='确定', width=8, command=mysort)
    button3 = tk.Button(root, text='退出', width=8, command=closeThisWindow)

    label1.pack()
    text1.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
