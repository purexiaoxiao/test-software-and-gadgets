import tkinter as tk
import ctodll
import draw
import labelme
import mp4togif
import toExeByspec
import todll
import toexe
import tozip
import ziptofile


def main():
	window = tk.Tk()
	window.geometry('500x300+570+200')
	bt1 = tk.Button(window, text='mp4文件转gif', command=mp4togif.main)
	bt2 = tk.Button(window, text='c++编译为dll文件', command=todll.main)
	bt3 = tk.Button(window, text='c编译为dll文件', command=ctodll.main)
	bt4 = tk.Button(window,
	                text='labelme标注后生成的json文件批量处理',
	                command=labelme.main)
	bt5 = tk.Button(window, text='画图小工具', command=draw.main)
	bt6 = tk.Button(window, text='压缩小工具', command=tozip.main)
	bt7 = tk.Button(window, text='解压小工具', command=ziptofile.main)
	bt8 = tk.Button(window, text='一键打包python文件小工具', command=toexe.main)
	bt9 = tk.Button(window,
	                text='一键打包python文件小工具通过.spec',
	                command=toExeByspec.main)
	bt1.pack()
	bt2.pack()
	bt3.pack()
	bt4.pack()
	bt5.pack()
	bt6.pack()
	bt7.pack()
	bt8.pack()
	bt9.pack()
	window.mainloop()


if __name__ == '__main__':
	main()
