def main():
    import tkinter as tk
    about = tk.Tk()
    about.title("关于")
    about.geometry('200x120')
    label1 = tk.Label(about, text='作者还很年轻')
    label2 = tk.Label(about, text='软件有bug的地方还请多包容')
    label3 = tk.Label(about, text='本小工具往后随缘更新')
    label4 = tk.Label(about, text='软件版本:0.1beta')
    button = tk.Button(about, text='确定', command=about.destroy)
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    button.pack()
    about.mainloop()


if __name__ == '__main__':
    main()
