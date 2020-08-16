def main():
    import os
    package = ['jpype1', 'moviepy', 'ctypes', 'pyinstaller', 'labelme']
    # for i in package:
    #     os.system('conda install ' + i)
    for i in package:
        os.system('pip install ' + i + ' -i https://pypi.doubanio.com/simple')


if __name__ == '__main__':
    main()
