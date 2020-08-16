def main():
    import jpype
    import os
    if not jpype.isJVMStarted():
        jpype.startJVM(jpype.getDefaultJVMPath(),
                       "-Djava.class.path=./factory.jar;./draw.jar",
                       convertStrings=True)
    jclass = jpype.JClass('com.Frame')
    jclass.main([])
    # os.system('pause')


if __name__ == '__main__':
    main()
