def main():
    import tkinter as tk
    import tkinter.filedialog
    import tkinter.messagebox
    import os
    import shutil

    def selectPath():
        nonlocal path_
        path_ = tk.filedialog.askopenfilenames(title='请选择xls文件',
                                               filetypes=[('xls文件', '.xls')])
        text1.delete(0, 'end')
        text1.insert(0, path_)

    def selectAnsPath():
        nonlocal ansPath
        ansPath = tk.filedialog.asksaveasfilename(title='请选择合并后的保存文件',
                                                  filetypes=[('xls文件', '.xls')
                                                             ])
        text2.delete(0, 'end')
        text2.insert(0, ansPath)

    def multipleFileToOne(filename1, filename2, ans):
        txt1 = open(filename1, 'r')

        txt2 = open(filename2, 'r')
        txt3 = open(ans, 'w')
        temp1 = txt1.readline().split('\t')  #读一行数据
        temp2 = txt2.readline().split('\t')  #读一行数据
        print('\t'.join(temp1), file=txt3)  #将第一行的标签先写入文件
        temp1 = txt1.readline().split('\t')  #开始读取学生信息数据
        temp2 = txt2.readline().split('\t')  #读一行学生信息数据
        while 1:
            try:  #捕捉读取EOF错误
                if int(temp1[-1]) > int(
                        temp2[-1]):  #如果第一个数据大于第二个则写入第二个 temp1继续读取一行数据
                    # print(temp1)
                    print('\t'.join(temp1), file=txt3, end='')
                    temp1 = txt1.readline().split('\t')
                else:  #反之写入第二个 temp2继续读取一行数据
                    # print(temp2)
                    print('\t'.join(temp2), file=txt3, end='')
                    temp2 = txt2.readline().split('\t')
            except:  #读到了eof
                break  #退出循环
        for i in txt1:  #保证temp1读完
            print(i, file=txt3, end='')
        txt1.close()  #关闭文件
        for i in txt2:  #保证temp2读完
            print(i, file=txt3, end='')
        txt2.close()
        txt3.close()

    def closeThisWindow():
        root.destroy()

    def begin():
        if len(path_) == 1:
            tk.messagebox.showerror('文件数量过少', '请选择多个xls文件')
            return
        elif path_ == '':
            tk.messagebox.showerror('路径为空', '请先选择文件')
            return
        if not os.path.isdir('./temp'):
            os.mkdir('./temp')
        multipleFileToOne(path_[0], path_[1], './temp//01.xls')  #首先归并0号和1号文件
        for num, i in enumerate(path_):  #num为计数器,i为路径
            if num == 0 or num == 1:  #0 1 已经合并完成
                continue
            multipleFileToOne('./temp/' + str(num - 2) + str(num - 1) + '.xls',
                              i, './temp/' + str(num - 1) + str(num) +
                              '.xls')  #合并
            # print(i)
            os.remove('.//temp/' + str(num - 2) + str(num - 1) +
                      '.xls')  #删除前一个合并结果
        shutil.copy('./temp/' + str(num - 1) + str(num) + '.xls',
                    ansPath + '.xls')  #(num-1)(num)即为ans  将答案复制到制定路径
        os.remove('./temp/' + str(num - 1) + str(num) + '.xls')  #删除最后一个临时文件
        os.removedirs('./temp')  #删除temp文件夹
        tk.messagebox.showinfo('完成', '文件合并完成')

    ansPath = ''
    path_ = ''
    root = tk.Tk()
    root.title('多文件合成小工具')  #窗口的标题
    root.geometry('500x300+570+200')
    label1 = tk.Label(root, text='请选择多个已排序文件:')
    label2 = tk.Label(root, text='请选择输出文件')
    text1 = tk.Entry(root, textvariable=path_, bg='white', width=45)
    button1 = tk.Button(root, text='浏览', width=8, command=selectPath)
    button2 = tk.Button(root, text='确定', width=8, command=begin)
    button3 = tk.Button(root, text='退出', width=8, command=closeThisWindow)
    text2 = tk.Entry(root, textvariable=ansPath, bg='white', width=45)
    button4 = tk.Button(root, text='浏览', width=8, command=selectAnsPath)
    label1.pack()
    text1.pack()
    button1.pack()
    label2.pack()
    text2.pack()
    button4.pack()
    button2.pack()
    button3.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
