import moviepy.editor as mpy
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import os


def begin():
    var = text1.get()
    try:
        if type(eval(var)) != int:
            tk.messagebox.showerror('输入错误', '您的输入错误请重新输入')
            return
    except:
        tk.messagebox.showerror('输入错误', '您的输入错误请重新输入')
        return
    tk.messagebox.showinfo('关机', '您的电脑将会在' + str(eval(var)) + 'min后关机')
    os.system('shutdown -s -t ' + str(int(var) * 60))


def end():
    root.quit()


root = tk.Tk()
root.title('关机小助手')  #窗口的标题
root.geometry('500x300+570+200')
label1 = tk.Label(root, text='请输入时间(min):')
text1 = tk.Entry(root, bg='white', width=10)
button2 = tk.Button(root, text='确定', width=8, command=begin)
button3 = tk.Button(root, text='取消', width=8, command=end)
label1.pack()
text1.pack()
button2.pack()
button3.pack()
root.mainloop()
